from main import db
from datetime import datetime
import enum

class AlbumType(enum.Enum):
    ALBUM = "ALBUM"
    SINGLE = "SINGLE"
    COMPILATION = "COMPILATION"

Album_Artist = db.Table("album_artist",
    db.Column('album_id', db.Integer, db.ForeignKey('albums.id')),
    db.Column('artist_id', db.Integer, db.ForeignKey('artists.id'))
)

class Album(db.Model):
    __tablename__ = "albums"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    album_type = db.Column(db.Enum(AlbumType), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False,default=datetime.now)
