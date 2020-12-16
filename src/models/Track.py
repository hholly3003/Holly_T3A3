from main import db

class Track(db.Model):
    __tablename__ = "tracks"

    track_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    track_num = db.Column(db.Integer, nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.album_id'))
    disc_num = db.Column(db.Integer, nullable=False)
    duration_ms = db.Column(db.Integer, nullable=False)
    explicit = db.Column(db.Boolean(), nullable=False)