#CODECLAUSE PVT LTD.
#Python Development Intern
#August-2023
#Golden Task-2

'''Library Management System'''

#SOURCE CODE

class Book:
    def __init__(self, title, author, quantity):
        self.title = title
        self.author = author
        self.quantity = quantity
        self.available = quantity


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, quantity):
        book = Book(title, author, quantity)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def view_books(self):
        print("Books in the library:")
        for index, book in enumerate(self.books, start=1):
            status = f"Available: {book.available}/{book.quantity}"
            print(f"{index}. '{book.title}' by {book.author} - {status}")

    def borrow_book(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if book.available > 0:
                book.available -= 1
                print(
                    f"You have borrowed '{book.title}' by {book.author}. Available: {book.available}/{book.quantity}")
            else:
                print("Sorry, no copies of the book are available for borrowing.")
        else:
            print("Invalid book index.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            quantity = int(input("Enter quantity of books to add: "))
            library.add_book(title, author, quantity)
        elif choice == '2':
            library.view_books()
        elif choice == '3':
            library.view_books()
            book_index = int(
                input("Enter the index of the book you want to borrow: "))
            library.borrow_book(book_index)
        elif choice == '4':
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#OUTPUT FORMAT
'''Library Management System
1. Add Book
2. View Books
3. Borrow Book
4. Quit
Enter your choice: 1
Enter book title: Ravana
Enter author name: Anees Mathur
Enter quantity of books to add: 10
Book 'Ravana' by Anees Mathur added to the library.

Library Management System
1. Add Book
2. View Books
3. Borrow Book
4. Quit
Enter your choice: 1
Enter book title: Werton
Enter author name: S.Werton
Enter quantity of books to add: 5
Book 'Werton' by S.Werton added to the library.

Library Management System
1. Add Book
2. View Books
3. Borrow Book
4. Quit
Enter your choice: 2
Books in the library:
1. 'Ravana' by Anees Mathur - Available: 10/10
2. 'Werton' by S.Werton - Available: 5/5

Library Management System
1. Add Book
2. View Books
3. Borrow Book
4. Quit
Enter your choice: 3
Books in the library:
1. 'Ravana' by Anees Mathur - Available: 10/10
2. 'Werton' by S.Werton - Available: 5/5
Enter the index of the book you want to borrow: 1
You have borrowed 'Ravana' by Anees Mathur. Available: 9/10

Library Management System
1. Add Book
2. View Books
3. Borrow Book
4. Quit
Enter your choice: 3
Books in the library:
1. 'Ravana' by Anees Mathur - Available: 9/10
2. 'Werton' by S.Werton - Available: 5/5
Enter the index of the book you want to borrow: 2
You have borrowed 'Werton' by S.Werton. Available: 4/5

Library Management System
1. Add Book
2. View Books
3. Borrow Book
4. Quit
Enter your choice: 4
Thank you for using the Library Management System. Goodbye!'''
