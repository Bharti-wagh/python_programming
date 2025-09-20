import tkinter as tk
from tkinter import ttk, messagebox
import csv, os
from datetime import datetime

FILENAME = "expenses.csv"

# CSV if not exists
def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "category", "amount", "description"])

#Add Expense
def add_expense():
    date = date_entry.get()
    if date.strip() == "":
        date = datetime.now().strftime("%Y-%m-%d")
    
    category = category_entry.get()
    amount = amount_entry.get()
    description = desc_entry.get()

    if category == "" or amount == "":
        messagebox.showerror("Error", "Category and Amount are required")
        return

    try:
        amount = float(amount)
    except:
        messagebox.showerror("Error", "Amount must be a number")
        return

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    messagebox.showinfo("Success", "Expense added successfully!")
    clear_entries()
    load_expenses()

#Load Expenses into Table
def load_expenses(filter_category=None):
    for row in tree.get_children():
        tree.delete(row)

    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if filter_category is None or row["category"].lower() == filter_category.lower():
                tree.insert("", "end", values=(row["date"], row["category"], row["amount"], row["description"]))

#Calculate Total
def show_total():
    total = 0
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["amount"])
    messagebox.showinfo("Total Expenses", f"💰 Total: {total}")

#Filter by Category
def filter_category():
    category = category_filter_entry.get()
    if category.strip() == "":
        load_expenses()
    else:
        load_expenses(category)

# Clear Input Fields
def clear_entries():
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)

#GUI Setup
init_file()
root = tk.Tk()
root.title("💰 Expense Tracker")
root.geometry("700x500")
root.resizable(False, False)

#Input Frame
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
date_entry = tk.Entry(frame)
date_entry.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
category_entry = tk.Entry(frame)
category_entry.grid(row=1, column=1, padx=5)

tk.Label(frame, text="Amount:").grid(row=2, column=0, padx=5, pady=5)
amount_entry = tk.Entry(frame)
amount_entry.grid(row=2, column=1, padx=5)

tk.Label(frame, text="Description:").grid(row=3, column=0, padx=5, pady=5)
desc_entry = tk.Entry(frame)
desc_entry.grid(row=3, column=1, padx=5)

add_btn = tk.Button(frame, text="Add Expense", command=add_expense, bg="lightgreen", width=20)
add_btn.grid(row=4, column=0, columnspan=2, pady=10)

# Table for Expenses
columns = ("Date", "Category", "Amount", "Description")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150 if col != "Description" else 250)
tree.pack(pady=10)

#Action Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

total_btn = tk.Button(btn_frame, text="Show Total", command=show_total, bg="lightblue", width=20)
total_btn.grid(row=0, column=0, padx=10)

tk.Label(btn_frame, text="Filter by Category:").grid(row=0, column=1)
category_filter_entry = tk.Entry(btn_frame)
category_filter_entry.grid(row=0, column=2, padx=5)
filter_btn = tk.Button(btn_frame, text="Apply Filter", command=filter_category, bg="orange", width=15)
filter_btn.grid(row=0, column=3, padx=5)

reset_btn = tk.Button(btn_frame, text="Reset", command=lambda: load_expenses(), bg="gray", width=15)
reset_btn.grid(row=0, column=4, padx=5)

#Load initial data
load_expenses()

root.mainloop()
