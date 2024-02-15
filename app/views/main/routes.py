from app.views.main import bp 
from flask import render_template,request
from flask_login import current_user
from app.views.main import utils
from app.models.book import Book
from app.views.trades.utils import Utils
from app.views.user import utils as user_utils
@bp.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        user=request.form['search']
        print(user)
        user_detail=user_utils.get_user(user)
        book=Book.recent_books()
        #current_trades=Utils.get_current_trades(current_user.id)
        return render_template('home/homepage.html',books=book,detail=user_detail)
    if current_user.is_authenticated:
        books=Book.recent_books()
        current_trades=Utils.get_current_trades(current_user.id)
        return render_template('home/homepage.html',books=books)
    else:
        return render_template('home/index.html')

@bp.route('/about')
def about():
    return render_template('home/about.html')
