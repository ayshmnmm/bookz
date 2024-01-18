import psycopg2 as pg
from config import Config

db = pg.connect(Config.POSTGRES_URL, keepalives=1, keepalives_idle=30, keepalives_interval=10, keepalives_count=5)
cursor = db.cursor()

with open('schema.sql', 'r') as f:
    cursor.execute(f.read())
    db.commit()
