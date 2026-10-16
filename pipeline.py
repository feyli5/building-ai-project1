"""
Smart Shelf Life - Food Dataset Annotation Parsing Prototype
Author: Okpe Levi Chinedu
Course: Building AI (University of Helsinki)
"""
import math
import json

# Simulated JSON payload typically exported from platforms like Label Studio
sample_annotation_data = """
{
    "image_id": "IMG_20261016_001.jpg",
    "annotations": [
        {"class": "apple", "bbox":, "storage_days": 6, "condition": "surface_spots"},
        {"class": "banana", "bbox":, "storage_days": 3, "condition": "good"}
    ]
}
"""

def parse_pipeline_data(json_input, storage_type="fridge"):
    """
    Parses labeled dataset items and scores real-time expiration metrics.
    Storage environment modifiers: fridge = 0.04 decay rate, pantry = 0.12 decay rate.
    """
    data = json.loads(json_input)
    decay_rate = 0.04 if storage_type == "fridge" else 0.12
    processed_items = []
    
    print(f"--- Processing Batch Image: {data['image_id']} ---")
    
    for item in data['annotations']:
        days = item['storage_days']
        
        # Core mathematical decay calculation
        freshness_pct = math.exp(-decay_rate * days) * 100
        rounded_freshness = round(freshness_pct, 1)
        
        status = "CRITICAL: Cook Immediately" if rounded_freshness < 65 else "Healthy"
        
        print(f"Detected Label: [{item['class'].upper()}] | BBox coordinates: {item['bbox']}")
        print(f" > Days Stored: {days} days | Est. Freshness: {rounded_freshness}% | Status: {status}\n")
        
        processed_items.append({"item": item['class'], "freshness": rounded_freshness})
        
    return processed_items

# Run the simulation pipeline locally
if __name__ == "__main__":
    parse_pipeline_data(sample_annotation_data, storage_type="pantry")
