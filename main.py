import admin
import user

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Book Title: ")
            author = input("Author: ")
            price = input("Price: ")
            admin.add_book(title, author, price)
        elif choice == "2":
            title = input("Book Title to Update: ")
            author = input("New Author (Enter for no change): ") or None
            price = input("New Price (Enter for no change): ") or None
            availability = input("Available? (y/n, Enter for no change): ")
            if availability.lower() == "y":
                availability = True
            elif availability.lower() == "n":
                availability = False
            else:
                availability = None
            admin.update_book(title, author, price, availability)
        elif choice == "3":
            title = input("Book Title to Delete: ")
            admin.delete_book(title)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def user_menu():
    while True:
        print("\n--- User Menu ---")
        print("1. Display Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == "1":
            user.display_books()
        elif choice == "2":
            title = input("Enter Book Title to Borrow: ")
            user.borrow_book(title)
        elif choice == "3":
            title = input("Enter Book Title to Return: ")
            user.return_book(title)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n=== Book Management System ===")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            admin_menu()
        elif choice == "2":
            user_menu()
        elif choice == "3":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
