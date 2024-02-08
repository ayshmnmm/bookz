from flask import Blueprint

bp = Blueprint('book',__name__)

from app.views.book import routes