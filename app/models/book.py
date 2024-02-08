from app.models import db,cursor

class Book:
    def recent_books(num=5):
        cursor.execute("SELECT * FROM books ORDER BY book_id DESC LIMIT %s", (num,))
        books= cursor.fetchall()
        return books