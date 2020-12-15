from main import db
from datetime import datetime
import enum

class AlbumType(enum.Enum):
    ALBUM = "ALBUM"
    SINGLE = "SINGLE"
    COMPILATION = "COMPILATION"

album_artist = db.Table("album_artist",
    db.Column('album_id', db.Integer, db.ForeignKey('albums.id')),
    db.Column('artist_id', db.Integer, db.ForeignKey('artists.id'))
)

class Album(db.Model):
    __tablename__ = "albums"

    album_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    album_type = db.Column(db.Enum(AlbumType), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False,default=datetime.now)
    album_artist = db.relationship("Artist", backref=db.backref("album_artist", lazy="dynamic"))
    tracks = db.relationship("Track", backref="album_id")
