# imports
from project import app, db
from project.models import BlogPost
from flask import flash, redirect, session, url_for, render_template, Blueprint
from flask.ext.login import login_required
from functools import wraps

# register blueprint
home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

# use decorators to link the function to a url
@home_blueprint.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)

@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')

