import sqlite3

class databaseconnection:
    def __int__(self):
        self.connection = None
    def __enter__(self):
        self.connection = sqlite3.connect("data.db")
        return self.connection
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
