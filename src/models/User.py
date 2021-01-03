from main import db, login_manager                                                                   # This is the db instance created by SQLAlchemy
from models.Profile import Profile                                                    # Importing the Profile model
from models.Playlist import Playlist                                                  # Importing the Playlist model
from models.Collection import Collection                                              # Importing the Collection model
from flask_login import UserMixin
from sqlalchemy.orm import backref                                                    # Used to make references to other tables

@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(int(user_id))
    return None

class User(db.Model, UserMixin):                                                                 # Creating a Users class inheriting from db.Model
    __tablename__= "users"                                                            # Explicitly naming the table "users"

    id = db.Column(db.Integer, primary_key=True)                                      # There is an id column and it is the primary key
    email = db.Column(db.String(), nullable=False, unique=True)                       # Email column, string and it must be unique
    password = db.Column(db.String(), nullable=False)                                 # The password is a string and must be present
    profile = db.relationship('Profile', backref=backref('user', uselist=False))      # Creating the relationship to the profile table
    playlists = db.relationship('Playlist', cascade= 'all, delete', backref='owner')
    collections = db.relationship('Collection', cascade='all, delete', backref='owner')
    is_admin = db.Column(db.Boolean(), default=False)

    def __repr__(self):                                                               # When printing the model we will see its email attribute
        return f"<User {self.email}>"