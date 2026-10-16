# 🍏 Smart Shelf Life: AI Freshness Tracker & Annotation Pipeline

## Summary
This is my final milestone project for the Building AI course. I designed an application concept called **Smart Shelf Life** to tackle household food waste. The system uses computer vision to track the freshness of groceries over time. To train the image recognition engine, the app processes raw bounding-box image annotations to identify distinct food items and evaluate surface degradation levels.

---

### 2. Why I wanted to build this
* **The Problem:** Households discard edible food daily simply because items get lost or forgotten in the back of the refrigerator drawers.
* **Frequency:** This is a recurring issue across millions of homes, leading to waste of money and increased greenhouse gas emissions in landfills.
* **My Motivation:** Working with AI data pipelines, I wanted to apply object tracking logic to automate grocery inventory tracking so users get smart alerts before their food spoils.

---

### 3. The Annotation & ML Pipeline (Python Prototype)
To train this AI model, the system must process object labels from an annotation platform (like Label Studio). Below is a Python script that prototypes this workflow. It loads an annotation record, extracts the item class, and runs an exponential decay algorithm to determine the freshness index.

```python
"""
Smart Shelf Life - Food Dataset Annotation Parsing Prototype
Author: Okpe Levi Chinedu
"""
import math
import json

# Simulated output JSON exported from an annotation platform like Label Studio
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

# Run the simulation pipeline
parse_pipeline_data(sample_annotation_data, storage_type="pantry")
```

---

### 4. How to Run and Test
If you want to run the python prototype locally on your computer:
1. Clone this repository or copy the code script into a local file named `pipeline.py`.
2. Open your terminal or command prompt and run:
   ```bash
   python pipeline.py
   ```
3. The script will output parsed classification results, bounding-box coordinate maps, and freshness tracking alerts directly to your terminal.

---

### 5. Application Workflow
* **Step 1:** The user takes a smartphone picture of their grocery haul.
* **Step 2:** The pipeline processes coordinates to isolate each food item inside the frame.
* **Step 3:** The app tracks the time elapsed and prompts the user with recipe recommendations when freshness scores drop under 30%.

Here is a visual example of the inventory environment:
![Groceries Layout Example](https://unsplash.com)

---

### 6. System Challenges
* **Occlusions:** When groceries are stacked or packed behind opaque boxes, the object detection model cannot see surface metrics to measure aging.
* **Ambient Variations:** Refrigerator settings fluctuate across different homes, which means static decay coefficients need adjustment based on localized user environments.

---

### 7. Next Steps & Future Plans
I intend to explore linking this annotation stream directly to point-of-sale receipt databases so that text data from digital receipts can automatically generate bounding box regions for incoming grocery lists.

---

### 8. Credits
* Built for the **Building AI course milestone project** (University of Helsinki / MinnaLearn).
* Implemented using data validation structures common in data label workflows.
