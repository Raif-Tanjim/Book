from utils import database

user_choice ="""
- 'a' to add a book
- 'i'to list books
- 'r' to mark as read
- 'd' to delete a book
- 'q' to quit
Your Choice:  """
def add_book():
    name = input("enter name: ")
    author = input("enter author: ")
    database.add_book(name, author)
def list():
    books = database.get_all_books()
    for book in books:
        read = "Done reading" if book['read'] else "Not read"
        print(f"{book['name']} by {book['author']} status: {read}")
def read_book():
    name = input("Enter the book you finished reading: ")
    database.mark_book(name)
def del_book():
    name = input("enter book: ")
    database.delete_book(name)
def menu():
    database.create_table()
    user_input = input(user_choice)
    while user_input != 'q':
        if user_input == 'a':
            add_book()
            print("added")
        elif user_input == 'i':
          print("Loading books......")
          list()
        elif user_input == 'r':
            read_book()
            print("marked as read")
        elif user_input == 'd':
            del_book()
        else:
            print("unknown choice")
        user_input = input(user_choice)

menu()