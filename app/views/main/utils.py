from app.models.book import Book

def fetch_recent_books(num=5):
    print(Book.recent_books())