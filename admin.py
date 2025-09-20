from file_manager import load_books, save_books

def add_book(title, author, price, filepath="books.csv"):
    books = load_books(filepath)
    if title in books:
        print("Book already exists!")
        return
    books[title] = {"author": author, "price": float(price), "availability": True}
    save_books(books, filepath)
    print(f"Book '{title}' added successfully.")


def update_book(title, author=None, price=None, availability=None, filepath="books.csv"):
    books = load_books(filepath)
    if title not in books:
        print("Book not found.")
        return
    if author:
        books[title]["author"] = author
    if price:
        books[title]["price"] = float(price)
    if availability is not None:
        books[title]["availability"] = availability
    save_books(books, filepath)
    print(f"Book '{title}' updated successfully.")


def delete_book(title, filepath="books.csv"):
    books = load_books(filepath)
    if title not in books:
        print("Book not found.")
        return
    del books[title]
    save_books(books, filepath)
    print(f"Book '{title}' deleted successfully.")
