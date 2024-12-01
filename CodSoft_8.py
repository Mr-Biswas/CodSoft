# Phase-2
# Project Title: Cafe management system

# Menu dictionary: Stores items with their prices
menu = {
    "Samosa": 55,
    "Paneer Tikka": 170,
    "Aloo Tikki": 60,
    "Onion Bhaji": 15,
    "Butter Chicken": 195,
    "Chicken Tikka Masala": 190,
    "Palak Paneer": 185,
    "Dal Tadka": 75,
    "Chole Bhature": 80,
    "Biriyani": 200,
    "Naan": 40,
    "Garlic Naan": 45,
    "Roti": 5,
    "Paratha": 10,
    "Plain Rice": 50,
    "Jeera Rice": 55,
    "Pulao": 65,
    "Gulab Jamun": 10,
    "Ras Malai": 70,
    "Kulfi": 25,
    "Mango Lassi": 60,
    "Masala Chai": 50,
    "Sweet Lassi": 55,
    "Coke": 20
}

# Printed a welcome message and the menu of drinks and snacks
print("-----------------------------------Welcome to Balwant Singh Dhaba-------------------------------------------------------")

# Printed each item and its price on a new line using a loop.The list comprehension [f"{item}: Rs{price}" for item, price in menu.items()] generates a list of formatted strings for each item in the menu dictionary.
print("\n".join([f"{item}: Rs{price}" for item, price in menu.items()]))

# Initialized order total to 0
order_total = 0

# First item order
# User input for first item
item1 = input("Enter the name of the item you want to order\n").title()

# Checked if the item exists in the menu
if item1 in menu:
    # If item is in menu, add its price to the total order
    order_total += menu[item1]
    print(f"Your item {item1} has been added to your cart")
else:
    print("Please order something from our menu")

# Loop to allow the user to order additional items
while True:
    # Asked if the customer wants to add another item
    an_order = input("Do you want to add another item? (Yes/No) ").capitalize()

    # If the customer wants to order another item
    if an_order == "Yes":
        # User input for next item
        item2 = input("Enter the name of next item:\n").title()

        # Checked if the second item is in the menu
        if item2 in menu:
            # Add price of second item to total
            order_total += menu[item2]
            print(f'Item {item2} has been ordered')
        else:
            # Handle invalid item
            print("Ordered item is out of the list")
    # If no more items are to be ordered
    elif an_order == "No":
        # Printed the total amount the customer has to pay
        print(f'The total amount to pay is Rs{order_total}')
        print("Thank You!! Visit Again")
        break
    # Exit the loop and end the program
