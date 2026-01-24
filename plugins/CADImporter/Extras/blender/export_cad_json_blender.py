# Copyright lAvArt Studio, 2026. All Rights Reserved.

import bpy
import json
import uuid
import os
from mathutils import Vector

# CAD Importer JSON Schema Version
SCHEMA_VERSION = "1.0"

def get_system_units():
    """
    Returns the system units as a string.
    Unreal CAD Importer expects: "mm", "cm", "m", "in", "ft"
    """
    settings = bpy.context.scene.unit_settings
    system = settings.system
    scale = settings.scale_length
    
    # Blender 'Metric' with scale 1.0 is Meters.
    # 'Imperial' with scale 1.0 is Feet? 
    # Let's try to deduce from scale and system.
    
    if system == 'METRIC':
        if abs(scale - 0.001) < 0.0001: return "mm"
        if abs(scale - 0.01) < 0.0001: return "cm"
        if abs(scale - 1.0) < 0.0001: return "m"
        if abs(scale - 1000.0) < 0.0001: return "km" # Not supported by importer, maybe fallback to m?
    elif system == 'IMPERIAL':
        # Imperial base is usually feet? 
        return "ft" # Fallback for now
        
    return "m" # Blender default is Meters

def get_obj_color(obj):
    # Blender objects can have color in multiple places:
    # 1. Object Color (Properties -> Viewport Display -> Color)
    # 2. Material (Viewport Display or Base Color)
    
    # We'll use Object Color
    c = obj.color
    return {
        "r": c[0],
        "g": c[1],
        "b": c[2],
        "a": c[3]
    }

def get_collection_name(obj):
    # Objects can be in multiple collections. We pick the first one basically.
    if len(obj.users_collection) > 0:
        return obj.users_collection[0].name
    return "Master Collection"

def apply_modifiers_to_curve(obj):
    # To get the final curve data with modifiers (like Geometry Nodes or Deformers),
    # we can use the Dependency Graph.
    depsgraph = bpy.context.evaluated_depsgraph_get()
    obj_eval = obj.evaluated_get(depsgraph)
    return obj_eval

def export_to_json(filepath, selected_only=False):
    print(f"Exporting to {filepath}...")
    
    doc = {
        "SchemaVersion": SCHEMA_VERSION,
        "SourceApp": "Blender",
        "Units": get_system_units(),
        "Layers": [],
        "Primitives": []
    }
    
    processed_layers = set()
    objects = bpy.context.selected_objects if selected_only else bpy.context.scene.objects
    
    count = 0
    
    for obj in objects:
        if obj.type != 'CURVE':
            # Could support FONT or MESH converted to Curve?
            # For now strictly CURVE
            continue
            
        # Get Evaluated Object (Apply Modifiers)
        obj_eval = apply_modifiers_to_curve(obj)
        data = obj_eval.data
        
        # Layer (Collection)
        layer_name = get_collection_name(obj)
        if layer_name not in processed_layers:
            processed_layers.add(layer_name)
            
            # Find collection visibility
            is_visible = True 
            # (Simplification: assumes visible)
            
            doc["Layers"].append({
                "Name": layer_name,
                "bVisible": is_visible,
                "Color": get_obj_color(obj)
            })
            
        # Extract Splines
        matrix = obj_eval.matrix_world
        
        for spline in data.splines:
            
            points_3d = []
            point_types = []
            arrive_tangents = []
            leave_tangents = []
            
            # Handle BEZIER
            if spline.type == 'BEZIER':
                if len(spline.bezier_points) < 2:
                    continue
                    
                for pt in spline.bezier_points:
                    # Apply World Transform
                    co = matrix @ pt.co
                    handle_left = matrix @ pt.handle_left
                    handle_right = matrix @ pt.handle_right
                    
                    # Convert Tangents
                    # Arrive = (Point - HandLeft) * 3
                    arrive = (co - handle_left) * 3.0
                    
                    # Leave = (HandRight - Point) * 3
                    leave = (handle_right - co) * 3.0
                    
                    points_3d.append({"x": co.x, "y": co.y, "z": co.z})
                    arrive_tangents.append({"x": arrive.x, "y": arrive.y, "z": arrive.z})
                    leave_tangents.append({"x": leave.x, "y": leave.y, "z": leave.z})
                    
                    # Type
                    # Blender has handle_left_type: FREE, VECTOR, ALIGNED, AUTO
                    p_type = 1 # Curve
                    if pt.handle_left_type == 'VECTOR' and pt.handle_right_type == 'VECTOR':
                        p_type = 0 # Corner
                        
                    point_types.append(p_type)
                    
            # Handle POLY (Linear)
            elif spline.type == 'POLY':
                if len(spline.points) < 2:
                    continue
                    
                for pt in spline.points:
                    co = matrix @ pt.co
                    
                    points_3d.append({"x": co.x, "y": co.y, "z": co.z})
                    
                    # Zero tangents for linear
                    arrive_tangents.append({"x": 0, "y": 0, "z": 0})
                    leave_tangents.append({"x": 0, "y": 0, "z": 0})
                    
                    point_types.append(0) # Linear
            
            # NURBS - Not fully supported yet, treated as Poly points
            elif spline.type == 'NURBS':
                 # Fallback to points as linear
                 if len(spline.points) < 2:
                    continue
                 for pt in spline.points:
                    # NURBS points have w (weight), ignoring for simple spline
                    co = matrix @ pt.co.to_3d() 
                    points_3d.append({"x": co.x, "y": co.y, "z": co.z})
                    arrive_tangents.append({"x": 0, "y": 0, "z": 0})
                    leave_tangents.append({"x": 0, "y": 0, "z": 0})
                    point_types.append(0)
            
            else:
                continue
                
            primitive = {
                "ID": str(uuid.uuid4()).replace('-', ''),
                "Type": "Spline",
                "LayerName": layer_name,
                "Points3D": points_3d,
                "PointTypes": point_types,
                "ArriveTangents": arrive_tangents,
                "LeaveTangents": leave_tangents,
                "bClosed": spline.use_cyclic_u or spline.use_cyclic_v,
                "Metadata": {
                    "ObjectName": obj.name
                }
            }
            
            doc["Primitives"].append(primitive)
            count += 1
            
    # Write
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(doc, f, indent=2)
        print(f"Success! Exported {count} splines to {filepath}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

class ExportCADJSON(bpy.types.Operator):
    """Export CAD Data to JSON"""
    bl_idname = "export.cad_json"
    bl_label = "Export CAD JSON"
    
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    
    def execute(self, context):
        export_to_json(self.filepath, selected_only=True)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

def register():
    bpy.utils.register_class(ExportCADJSON)
    # Add to menu
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    bpy.utils.unregister_class(ExportCADJSON)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

def menu_func_export(self, context):
    self.layout.operator(ExportCADJSON.bl_idname, text="CAD Importer JSON (.json)")

if __name__ == "__main__":
    register()
    # If run from main, trigger invoke
    # bpy.ops.export.cad_json('INVOKE_DEFAULT')
