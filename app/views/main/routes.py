from app.views.main import bp 
from flask import render_template
from flask_login import current_user

@bp.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('home/logged_in_index.html')
    else:
        return render_template('home/index.html')

@bp.route('/about')
def about():
    return render_template('home/about.html')
