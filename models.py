from . import db
from flask_login import UserMixin
from datetime import datetime as dt

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String)
    password = db.Column(db.String)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    question = db.Column(db.String)
    time = db.Column(db.DateTime, default=dt.now())
    
    