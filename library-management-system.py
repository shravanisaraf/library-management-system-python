import pandas as pd
import os

class Book:
    def __init__(self, title, author, borrowed=False):
        self.title = title
        self.author = author
        self.borrowed = borrowed

class Library:
    def __init__(self, filename):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            df = pd.read_excel(self.filename)
            books = []
            for index, row in df.iterrows():
                books.append(Book(row['Title'], row['Author'], row['Borrowed']))
            return books
        except FileNotFoundError:
            print("File not found. Creating a new library.")
            return []

    def save_books(self):
        try:
            book_data = {'Title': [book.title for book in self.books],
                         'Author': [book.author for book in self.books],
                         'Borrowed': [book.borrowed for book in self.books]}
            df = pd.DataFrame(book_data)
            df.to_excel(self.filename, index=False)
        except Exception as e:
            print("Error saving data:", e)

    def search_books(self):
        title = input("Enter book title to search: ")
        found_books = [book for book in self.books if book.title == title]
        if found_books:
            for book in found_books:
                print(f"Book found: {book.title} by {book.author}, Borrowed: {'Yes' if book.borrowed else 'No'}")
        else:
            print("Book not found.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        self.books.append(Book(title, author))
        self.save_books()
        print(f"{title} by {author} added to the library.")

    def remove_book(self):
        title = input("Enter book title to remove: ")
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                self.save_books()
                print(f"{title} removed from the library.")
                return
        print("Book not found.")

    def update_book_details(self):
        title = input("Enter book title to update: ")
        for book in self.books:
            if book.title == title:
                author = input("Enter new book author: ")
                book.author = author
                self.save_books()
                print(f"Details updated for {title}.")
                return
        print("Book not found.")

    def borrow_book(self):
        title = input("Enter book title to borrow: ")
        for book in self.books:
            if book.title == title:
                book.borrowed = True
                self.save_books()
                print(f"{title} borrowed from the library.")
                return
        print("Book not found.")

    def return_book(self):
        title = input("Enter book title to return: ")
        for book in self.books:
            if book.title == title:
                book.borrowed = False
                self.save_books()
                print(f"{title} returned to the library.")
                return
        print("Book not found.")

def main():
    filename = "books.xlsx"  # Change the filename to your Excel file
    library = Library(filename)

    while True:
        print("\nLibrary Management System")
        print("1. Search books")
        print("2. Add book")
        print("3. Remove book")
        print("4. Update book details")
        print("5. Borrow book")
        print("6. Return book")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            library.search_books()
        elif choice == "2":
            library.add_book()
        elif choice == "3":
            library.remove_book()
        elif choice == "4":
            library.update_book_details()
        elif choice == "5":
            library.borrow_book()
        elif choice == "6":
            library.return_book()
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
