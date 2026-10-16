# My Kitchen Freshness Tracker (Building AI Final Project)

This is my final milestone project for the Building AI course. I decided to make a simple app concept to solve a problem I deal with every single week in my own kitchen: throwing away food that got forgotten in the back of the fridge.

---

### 1. What my project does
My idea is called **Smart Shelf Life**. It is a straightforward mobile app concept where you take a quick photo of your groceries before putting them away. The app recognizes what the food is, estimates how many days it has left before spoiling, and sends a notification to your phone so you remember to cook it in time.

---

### 2. Why I wanted to build this
* **The Problem:** Like most people, I buy fresh fruits and veggies with good intentions, but they get buried behind other containers and go bad. It feels like a massive waste of money, and it is terrible for the environment when organic waste goes straight to a landfill.
* **How often it happens:** This happens to me and my friends almost every week. 
* **My Motivation:** I wanted to use basic AI concepts to handle the tracking for me so I don't have to constantly check expiration labels or open every drawer manually.

---

### 3. The AI parts and my code setup
To make this work, the system needs two steps:
1. **Recognizing the food item:** A standard image classification model (like a Convolutional Neural Network or CNN) to look at a photo and say "this is a banana" or "this is a carton of milk".
2. **Predicting the expiration date:** A basic regression setup that calculates a freshness score based on the storage type and how many days have passed.

I wrote a quick Python simulation to show how the freshness tracking logic works behind the scenes. It uses basic decay math based on where you store the item:

```python
# Simple Python simulation for my app's backend logic
import math

def check_my_groceries(days_in_kitchen, storage_place):
    # Pantry decays faster than the fridge
    if storage_place == "pantry":
        decay_rate = 0.15
    elif storage_place == "fridge":
        decay_rate = 0.05
    else:
        decay_rate = 0.02 # for freezer items
        
    # Standard formula to drop the percentage over time
    current_freshness = math.exp(-decay_rate * days_in_kitchen) * 100
    
    # Rounding it to make it clean for the user screen
    return round(current_freshness, 1)

# Testing my function to see if a tomato lasts 4 days in the pantry
print("Freshness left:")
print(check_my_groceries(4, "pantry"))
```

---

### 4. How a normal user uses it
* **Step 1:** You unpack your grocery bags and snap a single photo of your items.
* **Step 2:** The app registers the items and starts a countdown clock.
* **Step 3:** When a specific item drops below 25% freshness, you get an alert on your phone along with a couple of quick recipe ideas that use that exact ingredient.

Here is a quick placeholder layout of how I want the notification alert stream to look:
![App Layout Concept](https://tinyurl.com)

---

### 5. Main difficulties and challenges
* **Opaque Packaging:** If something is inside a cardboard box or a thick plastic container, a camera cannot see inside to check if the food is actually molding or stale. 
* **Temperature changes:** Fridges are set to different temperatures in every home, which means my fixed decay rates will need constant fine-tuning based on user settings.

---

### 6. Next steps for my project
I want to expand this idea by finding a way to link the app directly to digital grocery store receipts or store loyalty cards. That way, you wouldn't even have to take photos—your items would automatically load into your virtual fridge list the moment you pay at the checkout counter.

---

### 7. Credits
* This project was designed for the final section of the **Building AI course** organized by the University of Helsinki and MinnaLearn.
* The code simulation uses basic math principles covered in the regression modules of the course.
