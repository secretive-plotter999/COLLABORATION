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
