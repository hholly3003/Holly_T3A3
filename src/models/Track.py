from main import db

class Track(db.Model):
    __tablename__ = "tracks"

    track_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    track_num = db.Column(db.Integer)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.album_id"))
    disc_num = db.Column(db.Integer)
    duration_ms = db.Column(db.Integer)
    explicit = db.Column(db.Boolean())
