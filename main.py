import json
import os
from product import Product
from inventory import Inventory

FILENAME = "inventory.json"


# ---------- File handling ----------
def load_inventory():
    inventory = Inventory()
    if os.path.exists(FILENAME):
        print("inventory.json found.")
        with open(FILENAME, "r") as file:
            data = json.load(file)
        for item in data:
            inventory.add_product(Product.from_dict(item))
        print("Inventory loaded successfully.")
    else:
        print("No inventory.json found. Starting with empty inventory.")
    return inventory


def save_inventory(inventory):
    data = [product.to_dict() for product in inventory.get_products()]
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)
    print("Inventory saved successfully to inventory.json.")


# ---------- Menu actions (talk to the Inventory object) ----------
def add_product(inventory):
    new_id = input("Product ID: ")
    new_name = input("Product Name: ")
    try:
        new_price = float(input("Price: "))
        new_stock = int(input("Stock Quantity: "))
        product = Product(new_id, new_name, new_price, new_stock)
    except ValueError:
        print("Invalid input. Product not added.")
        return
    if inventory.add_product(product):
        print("Product added successfully!")
    else:
        print("A product with that ID already exists.")


def update_stock(inventory):
    product = inventory.search_product(input("Enter Product ID: "))
    if product is None:
        print("Product not found.")
        return
    print("Product Found:")
    print("Name:", product.get_name())
    print("Current Stock:", product.get_stock())
    try:
        product.update_stock(int(input("New Stock Quantity: ")))
        print("Stock updated successfully!")
    except ValueError:
        print("Invalid quantity. Stock not changed.")


def search_product(inventory):
    product = inventory.search_product(input("Enter Product ID: "))
    if product is None:
        print("Product not found.")
        return
    print("Product Found")
    print("------------------------------------------------")
    print("ID:", product.get_product_id())
    print("Name:", product.get_name())
    print("Price: $" + str(product.get_price()))
    print("Stock:", product.get_stock())
    print("------------------------------------------------")


# ---------- Main program ----------
def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()

    while True:
        print("----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")
        choice = input("Enter option: ")

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            save_inventory(inventory)
        elif choice == "6":
            save_inventory(inventory)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
