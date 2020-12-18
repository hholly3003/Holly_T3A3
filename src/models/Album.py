from main import db
from datetime import datetime
from models.Artist import Artist
from models.Track import Track
from models.AlbumType import AlbumType
from sqlalchemy.orm import backref 

album_artist = db.Table("album_artist",
    db.Column('album_id', db.Integer, db.ForeignKey('albums.album_id')),
    db.Column('artist_id', db.Integer, db.ForeignKey('artists.artist_id'))
)

class Album(db.Model):
    __tablename__ = "albums"

    album_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    album_type = db.relationship('AlbumType', backref=backref('album', uselist=False))
    release_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    album_artist = db.relationship('Artist', secondary=album_artist, backref=db.backref('album_artist', lazy='dynamic'))
    tracks = db.relationship('Track', backref='album')