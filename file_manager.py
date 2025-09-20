import csv
import os

FILEPATH = "books.csv"

def load_books(filepath=FILEPATH):
    """Load books from CSV into a dictionary."""
    books = {}
    if not os.path.exists(filepath):
        return books
    try:
        with open(filepath, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                books[row["title"]] = {
                    "author": row["author"],
                    "price": float(row["price"]),
                    "availability": row["availability"] == "True"
                }
    except Exception as e:
        print("Error reading file:", e)
    return books


def save_books(books, filepath=FILEPATH):
    """Save dictionary of books back to CSV."""
    with open(filepath, "w", newline="") as file:
        fieldnames = ["title", "author", "price", "availability"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for title, details in books.items():
            writer.writerow({
                "title": title,
                "author": details["author"],
                "price": details["price"],
                "availability": details["availability"]
            })
