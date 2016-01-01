# import the Flask class
from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
import sqlite3

# create the app object
app = Flask(__name__)

app.secret_key = "my precious"
app.database = "ample.db"

# Login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    posts = []
    try:
        g.db = connect_db()
        cur = g.db.execute('select * from posts')
#        posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
        for row in cur.fetchall():
            posts.append[dict(title=row[0], description=row[1])]
        g.db.close()
    except sqlite3.OperationalError:
        flash("You have no database!")

    return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in.')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out.')
    return redirect(url_for('welcome'))

def connect_db():
    return sqlite3.connect(app.database)

# start server with run() method
if __name__ == '__main__':
    app.run(debug=True)
