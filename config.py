from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
    POSTGRES_URL = os.environ.get('POSTGRES_URL')
    