import mysql.connector
import sys


def main():

    try:
        # Connection banane ki koshish
        conn = mysql.connector.connect(
            host="localhost", user="root", password="kanha123", database="store"
        )

        # Agar upar wali line bina error ke chal gayi, toh yeh message print hoga
        print("Success: Connected to Database!")

    except mysql.connector.Error as err:
        # Agar koi bhi error aata hai (galat password, server down, etc.)
        print(f"Error: Connection Failed! {err}")

        # App ko turant close karne ke liye
        sys.exit(1)

    cursor = conn.cursor()

    create_table = """CREATE TABLE IF NOT EXISTS product(
                        id INT PRIMARY KEY AUTO_INCREMENT, 
                        name VARCHAR(150) NOT NULL, 
                        category VARCHAR(100) NOT NULL, 
                        price DECIMAL(10,2) CHECK (price > 0)
                    )"""

    try:
        cursor.execute(create_table)
    except Exception as err:
        print(err)
    while True:
        print("Option 1. for create store")
        print("Option 2. for view store")
        print("Option 3. for update store")
        print("Option 4. for delete store")
        print("Option 5. for exit app")

        option = int(input("Choose Options: "))

        match (option):
            case 1:
                name = input("Enter product's name: ")
                category = input("Enter product's category: ")
                price = float(input("Enter product's price: "))
                insert_query = """INSERT INTO product (name, category, price) 
                            VALUES (%s, %s, %s)
                            """
                try:
                    cursor.execute(insert_query, (name, category, price))
                    conn.commit()
                    print("Product Inserted")
                except Exception as err:
                    print(err)
            case 2:
                try:
                    # Always commit any pending inserts before selecting to ensure data is visible
                    conn.commit()

                    cursor.execute("SELECT * FROM product")
                    rows = cursor.fetchall()
                    print(rows)

                    if not rows:
                        print("No products found in the database.")
                    else:
                        print("\n--- Product List ---")
                        for row in rows:
                            # Prints cleanly: ID: 1 | Name: Laptop | Category: Electronics | Price: 50000.00
                            print(
                                f"ID: {row[0]} | Name: {row[1]} | Category: {row[2]} | Price: {row[3]}"
                            )

                except Exception as err:
                    print(f"Error fetching data: {err}")

            case 3:
                pid = int(input("Enter product's id: "))
                newprice = float(input("Enter product's price: "))
                update_query = """UPDATE product SET price=%s WHERE id=%s"""
                try:
                    cursor.execute(update_query, (newprice, pid))
                    conn.commit()
                    print(f"Product updated successfully")
                except Exception as err:
                    print(err)
            case 4:
                pid = int(input("Enter product's id: "))
                delete_query = """DELETE FROM product WHERE id=%s"""
                try:
                    cursor.execute(delete_query, (pid,))
                    conn.commit()
                    print(f"Product deleted successfully")
                except Exception as err:
                    print(err)
            case 5:
                print("Your app have been closed")
                cursor.close()
                conn.close()
                print("Connection closed.")
                break
            case _:
                print("Wrong Option! Please Choose the Correct Option.")
                continue


if __name__ == "__main__":
    main()
