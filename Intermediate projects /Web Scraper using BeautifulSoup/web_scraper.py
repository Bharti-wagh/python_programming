import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

#SCRAPER FUNCTION
def scrape_website():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL")
        return
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad response
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch website:\n{e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    if not quotes:
        messagebox.showinfo("No Data", "No quotes found on this page.")
        return

    #Clear old data
    for row in tree.get_children():
        tree.delete(row)

    scraped_data.clear()

    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        tree.insert("", "end", values=(text, author))
        scraped_data.append([text, author])

#SAVE TO CSV
def save_to_csv():
    if not scraped_data:
        messagebox.showwarning("No Data", "Please scrape some data first!")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )

    if file_path:
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Quote", "Author"])
            writer.writerows(scraped_data)
        messagebox.showinfo("Success", f"Data saved to {file_path}")

#GUI
root = tk.Tk()
root.title("Web Scraper App")
root.geometry("800x500")
root.config(bg="#f4f6f9")

scraped_data = []

#URL Entry
frame_top = tk.Frame(root, bg="#f4f6f9")
frame_top.pack(pady=10)

tk.Label(frame_top, text="Enter URL:", font=("Arial", 12), bg="#f4f6f9").pack(side=tk.LEFT, padx=5)
url_entry = tk.Entry(frame_top, width=50, font=("Arial", 12))
url_entry.pack(side=tk.LEFT, padx=5)

scrape_btn = tk.Button(frame_top, text="Scrape", font=("Arial", 12), command=scrape_website, bg="#4CAF50", fg="white")
scrape_btn.pack(side=tk.LEFT, padx=5)

save_btn = tk.Button(frame_top, text="Save CSV", font=("Arial", 12), command=save_to_csv, bg="#2196F3", fg="white")
save_btn.pack(side=tk.LEFT, padx=5)

#Table
frame_table = tk.Frame(root)
frame_table.pack(pady=10, fill="both", expand=True)

columns = ("Quote", "Author")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=15)

tree.heading("Quote", text="Quote")
tree.heading("Author", text="Author")

tree.column("Quote", width=550, anchor="w")
tree.column("Author", width=200, anchor="center")

tree.pack(fill="both", expand=True)

root.mainloop()
