from flask import Flask, render_template, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db import User, Todo

app = Flask(__name__)
app.secret_key = "supersecretkey"

engine = create_engine('sqlite:///todo.db')
Session = sessionmaker(bind=engine)
db_session = Session()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods =[ 'GET', 'POST' ])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = db_session.query(User).filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            flash('Logged in successfully', 'info')

            

            
        else:
            flash('Incorrect username or password', 'danger')
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)


# 1 - deelte todo.db, recreate the database using db.py
# 2 - create a script using gpt - feed gpt your db.py schema and ask it to insert a user and some todos, then run the script
# 3 - test the login again
# 4 - create a dashboard.html page with a title
# 5 - create a route for the dashboard that will return the dashboard.html page and test it!!
# 6 - go to app.py and ask gpt to generate the code required to use the logged in user and grab the todos from the database
# 7 - go back to the dashboard html aand ask it to display the todos in a nice format