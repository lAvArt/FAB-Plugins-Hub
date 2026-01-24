# Copyright lAvArt Studio, 2026. All Rights Reserved.

import c4d
import json
import uuid
import os

# CAD Importer JSON Schema Version
SCHEMA_VERSION = "1.0"

def get_system_units(doc):
    """
    Returns the document units as a string.
    Unreal CAD Importer expects: "mm", "cm", "m", "in", "ft"
    """
    udata = doc.GetDataInstance()
    unit_id = udata[c4d.DOCUMENT_DOCUNIT]
    
    if unit_id == c4d.DOCUMENT_UNIT_MM: return "mm"
    if unit_id == c4d.DOCUMENT_UNIT_CM: return "cm"
    if unit_id == c4d.DOCUMENT_UNIT_M:  return "m"
    if unit_id == c4d.DOCUMENT_UNIT_INCH: return "in"
    if unit_id == c4d.DOCUMENT_UNIT_FOOT: return "ft"
    
    return "cm" # Default fallback

def get_layer_color(obj, doc):
    """
    Returns the display color of the object's layer, or the object's color if no layer.
    """
    layer = obj.GetLayerObject(doc)
    color = c4d.Vector(1, 1, 1) # Default White
    
    if layer:
        # Layer object Color
        color = layer[c4d.ID_BASEOBJECT_COLOR]
    else:
        # Object Color
        color = obj[c4d.ID_BASEOBJECT_COLOR]
        
    return {
        "r": color.x,
        "g": color.y,
        "b": color.z,
        "a": 1.0
    }

def get_layer_name(obj, doc):
    layer = obj.GetLayerObject(doc)
    if layer:
        return layer.GetName()
    return "Default"

def export_to_json(filepath, selected_only=False):
    doc = c4d.documents.GetActiveDocument()
    if not doc:
        return False
        
    print(f"Exporting to {filepath}...")
    
    export_data = {
        "SchemaVersion": SCHEMA_VERSION,
        "SourceApp": "Cinema 4D",
        "Units": get_system_units(doc),
        "Layers": [],
        "Primitives": []
    }
    
    processed_layers = set()
    objects_to_process = []
    
    if selected_only:
        objects_to_process = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    else:
        # Recursive collect function
        def collect_objects(op, collected):
            while op:
                collected.append(op)
                collect_objects(op.GetDown(), collected)
                op = op.GetNext()
        
        collect_objects(doc.GetFirstObject(), objects_to_process)
    
    count = 0
    
    for obj in objects_to_process:
        # Try to get a real spline representation (handles Primitives like Circle, Text, ect)
        spline = obj.GetRealSpline()
        
        if not spline:
            continue

        # Get Global Matrix for World Space transform
        mg = obj.GetMg()
            
        # Process Layer
        layer_name = get_layer_name(obj, doc)
        if layer_name not in processed_layers:
            processed_layers.add(layer_name)
            
            layer_obj = obj.GetLayerObject(doc)
            is_visible = True
            if layer_obj:
                is_visible = layer_obj.GetLayerData(doc)['view']
                
            export_data["Layers"].append({
                "Name": layer_name,
                "bVisible": is_visible,
                "Color": get_layer_color(obj, doc)
            })
            
        # Extract Spline Data
        # A SplineObject can have multiple segments
        segment_count = spline.GetSegmentCount()
        
        # If no segments explicitly defined, it treats the whole point list as one segment (unless closed logic applies)
        # But GetSegmentCount() returns 0 for simple single-segment splines in C4D sometimes? 
        # Actually checking SDK: "If 0, the spline has only one segment."
        if segment_count == 0:
            segment_count = 1
            
        all_points = spline.GetAllPoints()
        point_count = spline.GetPointCount()
        
        if point_count < 2:
            continue
            
        # Handling segments is tricky in C4D. 
        # Optimization: We will treat the C4D SplineObject as ONE primitive in JSON, 
        # BUT the JSON format expects a single continuous list of points.
        # If C4D spline has multiple segments, they are disconnected.
        # We should export each Segment as a SEPARATE primitive to match Unreal's SplineComponent logic (which is usually one loop).
        
        current_pt_index = 0
        
        for k in range(segment_count):
            # How many points in this segment?
            # C4D doesn't easily give "points per segment" via simple API in Python without Segment structure
            # Wait, SplineObject.GetSegment(id) returns dict info
            
            seg_info = {"cnt": point_count, "closed": spline[c4d.SPLINEOBJECT_CLOSED]} # Default if 0 segments
            if spline.GetSegmentCount() > 0:
                seg_info = spline.GetSegment(k)
            
            seg_points_count = seg_info["cnt"]
            is_closed = seg_info["closed"]
            
            if seg_points_count < 2:
                current_pt_index += seg_points_count
                continue
                
            points_3d = []
            point_types = []
            arrive_tangents = []
            leave_tangents = []
            
            for i in range(seg_points_count):
                pt_idx = current_pt_index + i
                pt = all_points[pt_idx] # c4d.Vector
                
                # Tangents
                # GetTangent returns dict: {'vl': Vector, 'vr': Vector} relative to the point
                vl = c4d.Vector(0,0,0)
                vr = c4d.Vector(0,0,0)
                
                if spline.GetTangentCount() > pt_idx:
                    try:
                        tangents = spline.GetTangent(pt_idx) 
                        vl = tangents['vl']
                        vr = tangents['vr']
                    except IndexError:
                        pass # Keep zero tangents

                # Transform to World Space
                pt = mg * pt
                vl = mg.MulV(vl)
                vr = mg.MulV(vr)
                
                # C4D Tangents to Unreal Tangents
                # Unreal Arrive = InVec. In C4D 'vl' is the handle pointing towards previous point.
                # In Unreal, Arrive Tangent is derivative vector entering the knot.
                # Arrive = (Point - PrevHandleWorldPos)
                # PrevHandleWorldPos = Point + vl
                # So Arrive = (Point - (Point + vl)) = -vl
                arrive = -vl * 4.0
                
                # Unreal Leave = OutVec. In C4D 'vr' is handle pointing towards next point.
                # Leave = (NextHandleWorldPos - Point)
                # NextHandleWorldPos = Point + vr
                # So Leave = ((Point + vr) - Point) = vr
                leave = vr * 4.0
                
                # Convert Y-Up (C4D) to Z-Up (Unreal)
                # We perform a -90 degree rotation around X-axis: (x, y, z) -> (x, -z, y)
                # This preserves handedness (unlike simple swizzling which mirrors).
                points_3d.append({"x": pt.x, "y": -pt.z, "z": pt.y})
                arrive_tangents.append({"x": arrive.x, "y": -arrive.z, "z": arrive.y})
                leave_tangents.append({"x": leave.x, "y": -leave.z, "z": leave.y})
                
                # Point Type
                # C4D stores interpolation per segment usually, but points can have soft/hard interpolation
                # We'll just assume Curve (1) unless we detect zero-length tangents, but safest is 1.
                # Checking strict zero might be good for corners.
                p_type = 1 # Curve
                if vl.GetLength() < 0.001 and vr.GetLength() < 0.001:
                    p_type = 0 # Linear/Corner
                
                point_types.append(p_type)
                
            current_pt_index += seg_points_count
            
            primitive = {
                "ID": str(uuid.uuid4()).replace('-', ''),
                "Type": "Spline",
                "LayerName": layer_name,
                "Points3D": points_3d,
                "PointTypes": point_types,
                "ArriveTangents": arrive_tangents,
                "LeaveTangents": leave_tangents,
                "bClosed": is_closed,
                "Metadata": {
                    "ObjectName": obj.GetName(),
                    "SegmentIndex": k
                }
            }
            
            export_data["Primitives"].append(primitive)
            count += 1
            
    # Write File
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2)
        print(f"Success! Exported {count} splines to {filepath}")
        c4d.gui.MessageDialog(f"Exported {count} splines successfully!")
        return True
    except Exception as e:
        print(f"Error writing file: {e}")
        c4d.gui.MessageDialog(f"Error exporting: {e}")
        return False


def show_ui():
    # Helper to pick file
    # c4d.storage.SaveDialog(title, force_suffix, def_file)
    fn = c4d.storage.SaveDialog(title="Export CAD JSON", force_suffix="json", def_file="Export.json")
    
    if not fn:
        return
        
    export_to_json(fn, selected_only=False)

# Execute main
show_ui()

