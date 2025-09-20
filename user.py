from file_manager import load_books, save_books

def display_books(filepath="books.csv"):
    books = load_books(filepath)
    if not books:
        print("No books available.")
        return
    for title, details in books.items():
        if details["availability"]:
            print(f"{title} by {details['author']} - ${details['price']}")
    print()


def borrow_book(title, filepath="books.csv"):
    books = load_books(filepath)
    if title in books and books[title]["availability"]:
        books[title]["availability"] = False
        save_books(books, filepath)
        print(f"You borrowed '{title}'.")
    else:
        print("Book not available.")


def return_book(title, filepath="books.csv"):
    books = load_books(filepath)
    if title in books and not books[title]["availability"]:
        books[title]["availability"] = True
        save_books(books, filepath)
        print(f"You returned '{title}'.")
    else:
        print("Book was not borrowed or does not exist.")
