import SQLAlchemy as SQLAlchemy
from flask import Flask
from app.user import LoginForm
from flask import render_template, flash, redirect, url_for
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'try-guessing'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/user/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {},remember_me={}'.format(form.email.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for admin {},remember_me={}'.format(form.email.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.before_first_request
def before_first_request():

    db.create_all()


if __name__ == 'main':
    app.run()
