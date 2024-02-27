from app.models import db,cursor
from app.models.user import User
import requests
from flask_login import current_user
class Book:
    def library_books(user_id):
        cursor.execute("SELECT b.book_id,b.book_name,b.author_name,b.image_url FROM book b,library l where (l.user_id=%s and l.book_id=b.book_id)",(user_id,))
        books=cursor.fetchall()
        book=[]
        for b in books:
            if b not in book:
                book.append(b)
        return book
    def get_by_id(book_id):
        response = requests.get("https://www.googleapis.com/books/v1/volumes/"+ book_id)
        data = response.json()
        volume_info = data.get('volumeInfo', {})
        description = volume_info.get('description', None)
        if description is not None:
                image_links = volume_info.get('imageLinks', {})
                thumbnail = image_links.get('thumbnail', '')

                book = {
                    'id': data.get('id', ''),
                    'title': volume_info.get('title', ''),
                    'authors': volume_info.get('authors', []),
                    'publishedDate': volume_info.get('publishedDate', ''),
                    'image_url': thumbnail,
                    'desc': volume_info.get('description'),
                    'page':volume_info.get('pageCount'),
                    'publishedDate':volume_info.get('publishedDate')
                }
                return book
    def recent_books():
        cursor.execute("SELECT u.id,u.username,u.city,b.book_id,b.book_name,b.author_name,b.image_url FROM book b,users u,library l where (l.user_id=u.id and l.book_id=b.book_id) ORDER BY book_id DESC LIMIT 10")
        books= cursor.fetchall()
        return books
    def insert_to_book(book_id):
        cursor.execute("SELECT * FROM book WHERE book_id=%s",(book_id,))
        b=cursor.fetchone()
        if not b:
            book=Book.get_by_id(book_id)
            first_author = book['authors'][0] if book.get('authors') else 'Unknown Author'
            cursor.execute("INSERT INTO book VALUES(%s,%s,%s,%s)",(book['id'],book['title'],first_author,book['image_url']))
            db.commit()
    def insert_to_lib(book_id):
        user_id = current_user.id
        cursor.execute("SELECT * FROM library WHERE book_id=%s and user_id=%s",(book_id,user_id))
        b=cursor.fetchall()
        if not b:
            cursor.execute("INSERT INTO library VALUES(%s,%s)",(user_id,book_id))
            db.commit()
    def get_by_name(book_name):
        cursor.execute("SELECT book_id FROM book WHERE book_name=%s",(book_name,))
        book=cursor.fetchone()
        return book