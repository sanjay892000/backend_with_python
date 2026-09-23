from services import *

def menu():
    print("\n==== Inventory System ====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Stock")
    print("4. Delete Product")
    print("5. Low Stock Alert")
    print("6. Exit")


while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Product name: ")
        qty = int(input("Quantity: "))
        price = float(input("Price: "))
        add_product(name, qty, price)
        print("✅ Product added")

    elif choice == "2":
        products = get_products()
        for p in products:
            print(p)

    elif choice == "3":
        pid = int(input("Product ID: "))
        qty = int(input("New quantity: "))
        update_stock(pid, qty)
        print("🔄 Updated")

    elif choice == "4":
        pid = int(input("Product ID: "))
        delete_product(pid)
        print("❌ Deleted")

    elif choice == "5":
        items = low_stock()
        print("\n⚠ Low Stock Items:")
        for i in items:
            print(i)

    elif choice == "6":
        break

    else:
        print("Invalid choice")