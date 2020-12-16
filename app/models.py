from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from app import db

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# User class table
class User(UserMixin,db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    username=db.Column(db.String(64), nullable=False,unique=True)
    fullname=db.Column(db.String(64),nullable=False)
    password_hash=db.Column(db.String(64), nullable=False)
    teamId=db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    meetings=db.relationship('Meeting',backref='booker',lazy='dynamic')
    participatings=db.relationship('Participants_user',backref='participater',lazy='dynamic')
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

# Team Class table
class Team(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    teamName=db.Column(db.String(64), nullable=False,unique=True)
    members=db.relationship('User',backref='team',lazy='dynamic')
    meetings=db.relationship('Meeting',backref='team',lazy='dynamic')

    def __repr__(self):
        return f'<Team {self.teamName}>'

# Room table and attributes
class Room(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    roomName=db.Column(db.String(64), nullable=False)
    meetings=db.relationship('Meeting',backref='room',lazy='dynamic')
    
    def __repr__(self):
        return f'Room {self.roomName}'

# Meeting table & attributes
class Meeting(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    title=db.Column(db.String(64),nullable=False,unique=True)
    teamId=db.Column(db.Integer, db.ForeignKey('team.id'))
    roomId=db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    bookerId=db.Column(db.Integer, db.ForeignKey('user.id'))
    date=db.Column(db.DateTime,nullable=False)
    startTime=db.Column(db.Integer,nullable=False)
    endTime=db.Column(db.Integer,nullable=False) 
    duration=db.Column(db.Integer,nullable=False)
    

    def __repr__(self):
        return f'Meeting {self.id} for {self.id} last for {self.duration}'

# participants table
class Participants_user(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    meeting=db.Column(db.String(64), db.ForeignKey('meeting.title'))
    userId=db.Column(db.Integer, db.ForeignKey('user.id'))
