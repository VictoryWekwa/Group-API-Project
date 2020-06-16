from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BoolenField, SubmitField
from wtforms.validators import DataRequired
from flask import db


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String())

    def __repr__(self):
        return '<User {}>'.format(self.email)


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BoolenField('Remember Me')
    submit = SubmitField('Sign In')