from main import db

class Artist(db.Model):
    __tablename__ = "artists"

    artist_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    uri = db.Column(db.String())