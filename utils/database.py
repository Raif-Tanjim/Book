from .connection import databaseconnection

def create_table():
    with databaseconnection() as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text,  read integer)")



def add_book(name, author):
    with databaseconnection() as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books VALUES(?, ?,  0)", (name, author))


def get_all_books():
    with databaseconnection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")
        books = [{"name": row[0],"author": row[1],"read": row[2]} for row in cursor.fetchall()]

    return books

def mark_book(name):
    with databaseconnection() as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE books SET read= 1 where name= ?", (name,))


def delete_book(name):
    with databaseconnection() as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM books where name= ?", (name,))
