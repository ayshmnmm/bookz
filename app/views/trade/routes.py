from flask import Blueprint, render_template, request, flash, redirect, url_for
import requests
from flask_login import login_required, current_user
from app.models import db, cursor
from app.views.trade import bp
API_BASE_URL = "https://www.googleapis.com/books/v1/volumes"