class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False

class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def register_patron(self, patron):
        self.patrons.append(patron)

    def borrow_book(self, patron, book):
        if book.borrow():
            patron.borrow_book(book)
            print(patron.name, "borrowed", book.title)
        else:
            print(book.title, "is already borrowed")

    def return_book(self, patron, book):
        if book in patron.borrowed_books:
            patron.return_book(book)
            book.return_book()
            print(patron.name, "returned", book.title)
        else:
            print(patron.name, "has not borrowed", book.title)


library = Library()

book1 = Book("Python Basics", "John Smith", "101")
book2 = Book("Data Structures", "Alice Brown", "102")

library.add_book(book1)
library.add_book(book2)

patron1 = Patron("Harsha", "P001")
patron2 = Patron("Rahul", "P002")

library.register_patron(patron1)
library.register_patron(patron2)

library.borrow_book(patron1, book1)
library.borrow_book(patron2, book1)
library.borrow_book(patron2, book2)

library.return_book(patron1, book1)

print("\nLibrary Books:")
for book in library.books:
    if book.is_borrowed:
        status = "Borrowed"
    else:
        status = "Available"
    print(book.title, "-", status)

print("\nPatron Details:")
for patron in library.patrons:
    print(patron.name, "has borrowed:")
    if patron.borrowed_books:
        for book in patron.borrowed_books:
            print("-", book.title)
    else:
        print("None")