import mysql.connector
from config import Config

db_config = {
    'host': Config.DB_HOST,
    'user': Config.DB_USER,
    'passwd': Config.DB_PASSWORD,
    'database': Config.DB_NAME
}

db = mysql.connector.connect(**db_config)
cursor = db.cursor()

# Ensure that the database is selected
cursor.execute(f'USE {Config.DB_NAME};')

with open('schema.sql', 'r') as f:
    # Execute the SQL script
    sql_script = f.read()
    for result in cursor.execute(sql_script, multi=True):
        if result.with_rows:
            print("Rows produced by statement '{}':".format(
                result.statement))
            print(result.fetchall())
        else:
            print("Number of rows affected by statement '{}': {}".format(
                result.statement, result.rowcount))

# Commit changes after executing the script
db.commit()
