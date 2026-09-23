import tkinter as tk
from tkinter import messagebox
import mysql.connector

# -------- DATABASE CONNECTION --------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="library_db"
)
cursor = conn.cursor()

# -------- FUNCTIONS --------

def add_book():
    title = entry_title.get()
    author = entry_author.get()

    if title == "" or author == "":
        messagebox.showerror("Error", "All fields required")
        return

    query = "INSERT INTO books (title, author) VALUES (%s, %s)"
    cursor.execute(query, (title, author))
    conn.commit()

    messagebox.showinfo("Success", "Book Added")
    clear_fields()


def view_books():
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    text_box.delete("1.0", tk.END)

    for row in rows:
        text_box.insert(tk.END,
            f"ID:{row[0]} | {row[1]} by {row[2]} | Status: {row[3]}\n")


def issue_book():
    book_id = entry_id.get()

    cursor.execute("UPDATE books SET status='Issued' WHERE id=%s", (book_id,))
    conn.commit()

    messagebox.showinfo("Success", "Book Issued")


def return_book():
    book_id = entry_id.get()

    cursor.execute("UPDATE books SET status='Available' WHERE id=%s", (book_id,))
    conn.commit()

    messagebox.showinfo("Success", "Book Returned")


def delete_book():
    book_id = entry_id.get()

    cursor.execute("DELETE FROM books WHERE id=%s", (book_id,))
    conn.commit()

    messagebox.showinfo("Success", "Book Deleted")


def clear_fields():
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_id.delete(0, tk.END)

# -------- GUI --------

root = tk.Tk()
root.title("Library Management System")
root.geometry("700x550")
root.configure(bg="#121212")  # dark theme

# Title
title = tk.Label(root, text="Library Management System",
                 font=("Arial", 20, "bold"),
                 bg="#121212", fg="#00ffcc")
title.pack(pady=15)

# Frame
frame = tk.Frame(root, bg="#1f1f2e", padx=20, pady=20)
frame.pack(pady=10)

# Inputs
tk.Label(frame, text="Book Title", bg="#1f1f2e", fg="white").grid(row=0, column=0)
entry_title = tk.Entry(frame)
entry_title.grid(row=0, column=1)

tk.Label(frame, text="Author", bg="#1f1f2e", fg="white").grid(row=1, column=0)
entry_author = tk.Entry(frame)
entry_author.grid(row=1, column=1)

tk.Label(frame, text="Book ID", bg="#1f1f2e", fg="white").grid(row=2, column=0)
entry_id = tk.Entry(frame)
entry_id.grid(row=2, column=1)

# Buttons
btn_add = tk.Button(root, text="Add Book", bg="#4CAF50", fg="white", command=add_book)
btn_add.pack(pady=5)

btn_view = tk.Button(root, text="View Books", bg="#2196F3", fg="white", command=view_books)
btn_view.pack(pady=5)

btn_issue = tk.Button(root, text="Issue Book", bg="#ff9800", fg="white", command=issue_book)
btn_issue.pack(pady=5)

btn_return = tk.Button(root, text="Return Book", bg="#9c27b0", fg="white", command=return_book)
btn_return.pack(pady=5)

btn_delete = tk.Button(root, text="Delete Book", bg="#f44336", fg="white", command=delete_book)
btn_delete.pack(pady=5)

# Output Box
text_box = tk.Text(root, width=80, height=12, bg="#1e1e1e", fg="white")
text_box.pack(pady=15)

root.mainloop()