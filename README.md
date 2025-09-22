# BookManagement
Book Management System is a Python project that lets Admins manage books (add, update, delete, set availability) and Users borrow or return them. Data is stored in a CSV file with error handling for invalid inputs, ensuring smooth and reliable book management.
# Book Management System

## 📌 Setup
1. Clone/download the project.
2. Ensure Python 3.x is installed.
3. Run:
   ```bash
   python main.py

## Features & Functionalities
#  Admin Module

1. Add new books with title, author, price, and availability.
2. Update existing book details.
3. Delete books from the system.
4. Manage availability (borrowed/available).

# User Module

1. View a list of available books.
2. Borrow a book (changes status to unavailable).
3. Return a book (changes status back to available).

# File Management

1. All book records are stored in books.csv.
2. Data is automatically updated when Admin/User actions are performed.

# Error Handling
Handles invalid inputs (e.g., non-existent books, wrong formats).

Recovers gracefully from missing or empty CSV files.

Ensures smooth user interaction with clear error messages.
