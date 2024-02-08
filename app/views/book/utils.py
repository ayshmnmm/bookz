import requests
from app.models import db,cursor

API_BASE_URL = 'https://www.googleapis.com/books/v1/volumes?q='

def search(name):
    response = requests.get(API_BASE_URL + name)
    data = response.json()
    items = data['items']
    books = []
    for item in items:
        volume_info = item.get('volumeInfo', {})
        description = volume_info.get('description', None)
        if description is not None:
            image_links = volume_info.get('imageLinks', {})
            thumbnail = image_links.get('thumbnail', '')

            book = {
                'id': item.get('id', ''),
                'title': volume_info.get('title', ''),
                'authors': volume_info.get('authors', []),
                'publishedDate': volume_info.get('publishedDate', ''),
                'image_url': thumbnail,
                'desc': description
            }
        if description is not None:
            books.append(book)
    return books   
def get_info_by_id(book_id):
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