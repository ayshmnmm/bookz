from flask import Blueprint

bp = Blueprint('main',__name__)

from app.views.main import routes
