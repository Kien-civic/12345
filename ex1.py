def restaurant_order_system():
    print("Welcome to the Restaurant Order Management System!")

    # Accept the type of meal
    meal_type = input("Please enter the type of meal (Pizza, Burger, Salad): ")

    # Check the type of meal and ask for additional options
    if meal_type == "Pizza":
        size = input("What size would you like? (Small, Medium, Large): ")
        if size not in ["Small", "Medium", "Large"]:
            print("Error: Invalid size selection.")
            return
        total_cost = calculate_cost(meal_type, size)

    elif meal_type == "Burger":
        cheese_choice = input("Do you want cheese? (Yes or No): ")
        if cheese_choice not in ["Yes", "No"]:
            print("Error: Invalid cheese selection.")
            return
        total_cost = calculate_cost(meal_type, cheese_choice)

    elif meal_type == "Salad":
        dressing = input("What type of dressing would you like? (Italian, Ranch, Caesar): ")
        if dressing not in ["Italian", "Ranch", "Caesar"]:
            print("Error: Invalid dressing selection.")
            return
        total_cost = calculate_cost(meal_type, dressing)

    else:
        print("Error: Meal type not recognized.")
        return

    # Display the total cost
    print(f"\nYour order summary:")
    print(f"Meal: {meal_type}")
    if meal_type == "Pizza":
        print(f"Size: {size}")
    elif meal_type == "Burger":
        print(f"Cheese: {cheese_choice}")
    elif meal_type == "Salad":
        print(f"Dressing: {dressing}")
    print(f"Total Cost: ${total_cost}")

def calculate_cost(meal_type, option):
    # Fixed prices for each item and option
    prices = {
        "Pizza": {"Small": 10, "Medium": 12, "Large": 15},
        "Burger": {"Yes": 8, "No": 6},
        "Salad": {"Italian": 7, "Ranch": 8, "Caesar": 9},
    }
    return prices[meal_type][option]

# Run the order system
restaurant_order_system()