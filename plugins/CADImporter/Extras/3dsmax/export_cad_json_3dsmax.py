
# Copyright lAvArt Studio, 2026. All Rights Reserved.

import os
import json
import uuid
from pymxs import runtime as rt

# CAD Importer JSON Schema Version
SCHEMA_VERSION = "1.0"

def get_color_from_layer(layer):
    c = layer.wirecolor
    return {
        "r": c.r / 255.0,
        "g": c.g / 255.0,
        "b": c.b / 255.0,
        "a": 1.0
    }

def get_system_units():
    # Helper to get unit string string
    # We export points as-is (System Units), but tell Unreal what they are
    # Unreal CAD Importer expects: "mm", "cm", "m", "in", "ft"
    
    # 3ds Max System Units
    # units.SystemType: #Inches, #Feet, #Miles, #Millimeters, #Centimeters, #Meters, #Kilometers
    ut = rt.units.SystemType
    if ut == rt.Name("Millimeters"): return "mm"
    if ut == rt.Name("Centimeters"): return "cm"
    if ut == rt.Name("Meters"): return "m"
    if ut == rt.Name("Inches"): return "in"
    if ut == rt.Name("Feet"): return "ft"
    return "cm" # Default fallback

def export_to_json(filepath, selected_only=False):
    print(f"Exporting to {filepath}...")
    
    doc = {
        "SchemaVersion": SCHEMA_VERSION,
        "SourceApp": "3ds Max",
        "Units": get_system_units(),
        "Layers": [],
        "Primitives": []
    }
    
    # Collect Layers and Primitives
    processed_layers = set()
    
    objects_to_export = rt.selection if selected_only else rt.objects
    
    count = 0
    
    for obj in objects_to_export:
        if not rt.superClassOf(obj) == rt.Shape:
            continue
            
        # Create a temporary copy to convert to SplineShape
        # This ensures we handle Circles, Rectangles, Text, etc. correctly
        # and applies modifiers/transforms to the data we read.
        try:
            temp_obj = rt.copy(obj)
            rt.convertToSplineShape(temp_obj)
        except Exception as e:
            print(f"Failed to convert {obj.name}: {e}")
            if temp_obj: rt.delete(temp_obj)
            continue

        # Determine Layer
        layer = obj.layer
        layer_name = layer.name
        
        if layer_name not in processed_layers:
            processed_layers.add(layer_name)
            doc["Layers"].append({
                "Name": layer_name,
                "bVisible": not layer.isHidden,
                "Color": get_color_from_layer(layer)
            })
            
        # Extract Splines from the temporary SplineShape
        num_splines = rt.numSplines(temp_obj)
        
        for s_idx in range(1, num_splines + 1):
            num_knots = rt.numKnots(temp_obj, s_idx)
            if num_knots < 2: 
                continue
                
            points_3d = []
            
            point_types = []
            arrive_tangents = []
            leave_tangents = []
            
            for k in range(1, num_knots + 1):
                # getKnotPoint returns World Space coordinates for SplineShape
                pt = rt.getKnotPoint(temp_obj, s_idx, k)
                ktype = rt.getKnotType(temp_obj, s_idx, k)
                
                # Handles
                in_vec = rt.getInVec(temp_obj, s_idx, k)
                out_vec = rt.getOutVec(temp_obj, s_idx, k)
                
                # Calculate Tangents (Bezier Handle -> Hermite Tangent)
                # Unreals ArriveTangent: Vector entering the knot (follows curve direction)
                # Max InVec is the handle position "before" the knot.
                # So Vector = (Knot - InVec) * 3.0
                arrive_x = (pt.x - in_vec.x) * 3.0
                arrive_y = (pt.y - in_vec.y) * 3.0
                arrive_z = (pt.z - in_vec.z) * 3.0
                
                # Unreal LeaveTangent: Vector leaving the knot.
                # Max OutVec is the handle position "after" the knot.
                # So Vector = (OutVec - Knot) * 3.0
                leave_x = (out_vec.x - pt.x) * 3.0
                leave_y = (out_vec.y - pt.y) * 3.0
                leave_z = (out_vec.z - pt.z) * 3.0
                
                arrive_tangents.append({"x": arrive_x, "y": arrive_y, "z": arrive_z})
                leave_tangents.append({"x": leave_x, "y": leave_y, "z": leave_z})

                # specific types: #corner, #smooth, #bezier, #bezierCorner
                # Map to Int: 0 = Linear/Corner, 1 = Curve/Smooth
                p_type = 0 if ktype == rt.Name("corner") else 1
                point_types.append(p_type)
                
                points_3d.append({
                    "x": pt.x, 
                    "y": pt.y, 
                    "z": pt.z
                })
            
            is_closed = rt.isClosed(temp_obj, s_idx)
            
            primitive = {
                # Remove hyphens for Unreal FGuid compatibility
                "ID": str(uuid.uuid4()).replace('-', ''),
                "Type": "Spline",
                "LayerName": layer_name,
                "Points3D": points_3d,
                "PointTypes": point_types,
                "ArriveTangents": arrive_tangents,
                "LeaveTangents": leave_tangents,
                "bClosed": is_closed,
                "Metadata": {
                    "ObjectName": obj.name
                }
            }
            
            doc["Primitives"].append(primitive)
            count += 1
            
        # Cleanup temp object
        rt.delete(temp_obj)
            
    # Write File
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(doc, f, indent=2)
        print(f"Success! Exported {count} splines.")
        return True
    except Exception as e:
        print(f"Error writing file: {e}")
        return False

# Example usage UI
def show_ui():
    # Simple rollout
    # For now, just a script that can be run
    # Let's prompt for file
    
    filename = rt.getSaveFileName(
        caption="Export CAD JSON",
        filename="Export.json",
        types="JSON Files (*.json)|*.json|All Files (*.*)|*.*|"
    )
    
    if filename:
        export_to_json(filename, selected_only=(rt.selection.count > 0))

if __name__ == "__main__":
    show_ui()
