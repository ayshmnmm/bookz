from app import create_app

app = create_app()

app.config['POSTGRES_URL'] = 'mysql://root:password123@localhost/mydb'
app.config['SECRET_KEY']='a random string'
if __name__ == '__main__':
    app.run(debug=True)
    