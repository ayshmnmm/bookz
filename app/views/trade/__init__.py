from flask import Blueprint

bp=Blueprint("trade",__name__)

from app.views.trade import routes