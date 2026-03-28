# Q: 3 Assignment — Part 2: Data Structures
# Theme: Restaurant Menu & Order Management System

# ================== Provided Data ==================

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

def print_task(title):
    print("\n" + "="*50)
    print(title)
    print("="*50 + "\n")

# ================== PART 1: GROUP BY CATEGORY ==================
print_task("Task 1 — Explore the Menu")

# Step 1: Get unique categories using set
categories = set(item["category"] for item in menu.values())

# Step 2: Loop through each category
categories = ["Starters", "Mains", "Desserts"]
for category in categories:
    print(f"\n===== {category} =====")
        
    # Step 3: Loop through menu and print items of that category
    
    for name, details in menu.items():
        
        if details["category"] == category:
            
            # Step 4: Check availability
            status = "Available" if details["available"] else "Unavailable"
            
            # Step 5: Print item details
            print(f"{name}  ₹{details['price']}  [{status}]")
            


# ================== PART 2: CALCULATIONS ==================

# Total number of items
total_items = len(menu)

# Total available items
available_items = sum(1 for item in menu.values() if item["available"])

# Most expensive item
most_expensive = max(menu.items(), key=lambda x: x[1]["price"])

# Items under ₹150 (sorted ascending by price)
under_150 = sorted(
    [(name, details["price"]) for name, details in menu.items() if details["price"] < 150],
    key=lambda x: x[1]
)

# ================== PRINT RESULTS ==================

print("\n===== SUMMARY =====")
print("Total items:", total_items)
print("Available items:", available_items)

print("Most expensive item:", most_expensive[0], "₹", most_expensive[1]["price"])

print("Items under ₹150:")
for item in under_150:
    print(item[0], "₹", item[1])

#--------------------------------------------------------------------------------------------------------------------
# Task 2 — Cart Operations
print_task("Task 2 — Cart Operations")
# ================== CART ==================
cart = []

# ================== ADD ITEM ==================
def add_to_cart(item_name, qty):
    
    # Convert input to lowercase for comparison
    item_name = item_name.lower()

    # Find correct item from menu
    found_item = None
    for name in menu:
        if name.lower() == item_name:
            found_item = name
            break

    # If item not found
    if not found_item:
        print(f"{item_name} not found in menu")
        return
    
    # Check availability
    if not menu[found_item]["available"]:
        print(f"{found_item} is unavailable")
        return
    
    # If already in cart → increase quantity
    for item in cart:
        if item["item"] == found_item:
            item["quantity"] += qty
            print(f"Updated {found_item} to {item['quantity']}")
            return
    
    # Add new item
    cart.append({
        "item": found_item,
        "quantity": qty,
        "price": menu[found_item]["price"]
    })
    print(f"\nAdded {found_item} x{qty}")


# ================== REMOVE ITEM ==================
def remove_from_cart(item_name):
    
    item_name = item_name.lower()

    for item in cart:
        if item["item"].lower() == item_name:
            cart.remove(item)
            print(f"Removed {item['item']}")
            return
    
    print(f"{item_name} not in cart")


# ================== UPDATE QUANTITY ==================
def update_quantity(item_name, qty):
    
    item_name = item_name.lower()

    for item in cart:
        if item["item"].lower() == item_name:
            item["quantity"] = qty
            print(f"{item['item']} quantity updated to {qty}")
            return
    
    print(f"{item_name} not in cart")


# ================== PRINT CART ==================
def print_cart():
    print("\n--- CART ---")
    if not cart:
        print("Cart is empty")
        return
    
    for item in cart:
        print(f"{item['item']} x{item['quantity']} ₹{item['price']}")
    
    print("----------------")



# ================== TESTING ==================

# Changed the quantity 2 in the question to 7 to stimulate alert reorder alert in task 3

add_to_cart("Paneer Tikka", 7)
print_cart()

add_to_cart("Gulab Jamun", 1)
print_cart()

add_to_cart("Paneer Tikka", 1)
print_cart()

add_to_cart("Mystery Burger", 1)
print_cart()

add_to_cart("Chicken Wings", 1)
print_cart()

remove_from_cart("Gulab Jamun")
print_cart()



# ================== Order Summary ==================

def order_summary():
    print("\n========= Order Summary =========")
    
    subtotal = 0
    
    for item in cart:
        item_total = item["quantity"] * item["price"]
        subtotal = subtotal + item_total
        print(f"{item['item']} x{item['quantity']} ₹{item_total}")
    
    print("--------------------------------")
    print(f"Subtotal: ₹{subtotal:.2f}")
    
    gst = subtotal * 0.05
    print(f"GST (5%): ₹{gst:.2f}")
    
    total = subtotal + gst
    print(f"Total Payable: ₹{total:.2f}")
    print("================================")

order_summary()

#----------------------------------------------------------------------------------------

# Task 3 — Inventory Tracker with Deep Copy

print_task("Task 3 — Inventory Tracker with Deep Copy")

import copy
# ================== STEP 1: DEEP COPY ==================
inventory_backup = copy.deepcopy(inventory)

# Change one value to prove deep copy
inventory["Paneer Tikka"]["stock"] = 5

print("Original Inventory Changed:")
print(f"Paneer Tikka -> {inventory['Paneer Tikka']}")

print("\nBackup Inventory (unchanged):")
print(f"Paneer Tikka -> {inventory_backup['Paneer Tikka']}")


# Restore original inventory
inventory = copy.deepcopy(inventory_backup)


# ================== STEP 2: ORDER FULFILLMENT ==================
print("\n--- Order Fulfillment ---")

# Use final cart from Task 2
# Example cart (Actual cart will already exist)
# cart = [{"item": "Paneer Tikka", "quantity": 8, "price": 180.0}]

for item in cart:
    name = item["item"]
    qty = item["quantity"]
    stock = inventory[name]["stock"]

    if qty > stock:
        print(f"⚠ Only {stock} available for {name}")
        inventory[name]["stock"] = 0
    else:
        inventory[name]["stock"] -= qty


# ================== STEP 3: REORDER ALERT ==================
print("\n--- Reorder Alerts ---")

for name, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(f"⚠ Reorder Alert: {name} — Only {details['stock']} unit(s) left (reorder level: {details['reorder_level']})")


# ================== STEP 4: FINAL PRINT ==================
print("\nFinal Inventory:")
for name, details in inventory.items():
    print(name, details)

print("\nBackup Inventory (unchanged):")
for name, details in inventory_backup.items():
    print(name, details)

#--------------------------------------------------------------------------------------

# Task 4 — Daily Sales Log Analysis

print_task("Task 4 — Daily Sales Log Analysis")


# ================== 1. REVENUE PER DAY ==================
print("--- Revenue Per Day ---")

daily_revenue = {}

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    print(date, "₹", total)


# ================== 2. BEST SELLING DAY ==================
best_day = max(daily_revenue, key=daily_revenue.get)
print("\nBest Selling Day:", best_day, "₹", daily_revenue[best_day])


# ================== 3. MOST ORDERED ITEM ==================
item_count = {}

for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_count[item] = item_count.get(item, 0) + 1

most_ordered = max(item_count, key=item_count.get)
print("\nMost Ordered Item:", most_ordered)


# ================== 4. ADD NEW DAY ==================
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\n--- Updated Revenue Per Day ---")

daily_revenue = {}
for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    print(date, "₹", total)

best_day = max(daily_revenue, key=daily_revenue.get)
print("\nUpdated Best Selling Day:", best_day, "₹", daily_revenue[best_day])


# ================== 5. NUMBERED ORDER LIST ==================
print("\n--- All Orders ---")

count = 1

for date, orders in sales_log.items():
    for order in orders:
        items = ", ".join(order["items"])
        
        print(f"{count:<3} [{date}] Order #{order['order_id']:<2} "
              f"₹{order['total']:<6.2f} - Items: {items}")
        
        count = count + 1

