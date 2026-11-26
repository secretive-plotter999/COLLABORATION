print("POS ORDERING SYSTEM")

print("Product Menu")
print("No.\tProduct\t\tPrice")
print("1\tBurger\t\tP50.00")
print("2\tFries\t\tP35.00")
print("3\tSoft Drink\tP25.00")
print("4\tItlog Ni Sean\tP1000.00")

while True:
    choice = input("\nEnter the product number (1-3): ")

    if choice == "1":
        product_name = "Burger"
        product_price = 50.00
    elif choice == "2":
        product_name = "Fries"
        product_price = 35.00
    elif choice == "3":
        product_name = "Itlog Ni Sean"
        product_price = 1000.00
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity < 1:
        print("Quantity must be at least 1.")
        continue

    subtotal = product_price * quantity

    print("Product:", product_name)
    print("Quantity:", quantity)
    print("Subtotal: P", format(subtotal, ".2f"))

    another = input("Order another product? (yes/no): ").lower()
    if another != "yes":
        break
def calculate_total(orders):
    """Calculate the total amount to be paid from a list of ordered items."""
    total = 0.0
    for item in orders:
        subtotal = item.get("subtotal", item["price"] * item["quantity"])
        total += subtotal
    return total


def print_receipt(orders, store_name="Small Store POS"):
    """Display a formatted receipt with items, quantities, prices, subtotals, and total."""
    print("\n" + "=" * 52)
    print(f"{store_name.upper():^52}")
    print("=" * 52)

    if not orders:
        print("No items ordered.")
        print("=" * 52)
        return

    print(f"{'Item':<18} {'Qty':>5} {'Price':>10} {'Subtotal':>12}")
    print("-" * 52)

    for item in orders:
        name = item["name"]
        qty = item["quantity"]
        price = item["price"]
        subtotal = item.get("subtotal", price * qty)
        print(f"{name:<18} {qty:>5} ₱{price:>9.2f} ₱{subtotal:>11.2f}")

    total_amount = calculate_total(orders)
    print("-" * 52)
    print(f"{'TOTAL AMOUNT TO PAY:':<39} ₱{total_amount:>10.2f}")
    print("=" * 52)


# Standalone test block (runs only when testing this file directly)
if _name_ == "_main_":
    sample_orders = [
        {"name": "Burger", "price": 50.00, "quantity": 2, "subtotal": 100.00},
        {"name": "Fries", "price": 35.00, "quantity": 1, "subtotal": 35.00},
        {"name": "Soft Drink", "price": 25.00, "quantity": 3, "subtotal": 75.00},
    ]
    print_receipt(sample_orders, store_name="CS3 Mini Store")
