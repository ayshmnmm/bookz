import psycopg2 as pg
from config import Config

db = pg.connect(Config.POSTGRES_URL)
cursor = db.cursor()

with open('schema.sql', 'r') as f:
    cursor.execute(f.read())
    db.commit()
