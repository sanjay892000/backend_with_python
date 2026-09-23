import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # change if needed
    password="1234",
    database="student_db"
)

cursor = conn.cursor()

# -------- FUNCTIONS -------- #

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"

    values = (name, age, course)
    cursor.execute(query, values)
    conn.commit()
    print("Student added successfully!\n")


def view_students():
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()

    print("\n--- Student List ---")
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")
    print()


def update_student():
    student_id = int(input("Enter student ID to update: "))
    new_course = input("Enter new course: ")

    query = "UPDATE students SET course=%s WHERE id=%s"
    cursor.execute(query, (new_course, student_id))
    conn.commit()

    print("Student updated!\n")


def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (student_id,))
    conn.commit()

    print("Student deleted!\n")


# -------- MENU -------- #

while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice!\n")

# Close connection
cursor.close()
conn.close()