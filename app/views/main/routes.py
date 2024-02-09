from app.views.main import bp 
from flask import render_template
from flask_login import current_user
from app.views.main import utils

@bp.route('/')
def index():
    if current_user.is_authenticated:
        books=utils.fetch_recent_books()
        return render_template('home/homepage.html',books=books)
    else:
        return render_template('home/index.html')

@bp.route('/about')
def about():
    return render_template('home/about.html')
