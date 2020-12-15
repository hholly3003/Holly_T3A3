from main import db
from models.Track import Track

playlist_track = db.Table("playlist_track",
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.id'))
    db.Column('track_id', db.Integer, db.ForeignKey('tracks.id'))
)

class Playlist(db.Model):
    __tablename__ = "playlists"

    playlist_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable = False)
    owner = db.Column(db.Integer,db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String())
    collaborative = db.Column(db.Boolean())
    public = db.Column(db.Boolean())
    playlist_track = db.relationship('Track', secondary=playlist_track, backref=db.backref('playlist_track', lazy='dynamic'))