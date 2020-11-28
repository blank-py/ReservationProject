# File Name: user.py
# Original Author: Jesse Malinen/blank-py
# Description: User model

# imports
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable = False, unique=True)
    email = db.Column(db.String(200), nullable = False, unique = True)
    password = db.Column(db.String(200))
    
    reservations = db.relationship('Reservation', backref='users')
    
    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()