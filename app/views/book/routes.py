from app.views.book import bp
from flask import render_template,request
from app.models.book import Book
from app.views.book import utils


@bp.route('/search',methods=['GET','POST'])
def search_book():
    if request.method=='POST':
        book_name=request.form['book_name']
        detail=utils.search(book_name)
        return render_template('book/search.html',detail=detail)
    return render_template('home/homepage.html')
@bp.route('/')
def add_book():
    pass

@bp.route('/j')
def remove_book():
    pass

@bp.route('/info/<book_id>')
def book_info(book_id):
    if  book_id:
        detail=utils.get_info_by_id(book_id)
        print(detail)
        return render_template('book/info.html',det=detail)
    return render_template('book/search.html') 