from main import db

class AlbumType(db.Model):
    __tablename__ = "album_types"

    at_id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.album_id'), nullable=False)
