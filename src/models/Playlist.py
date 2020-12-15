from main import db
from models.Track import Track

playlist_tracks = db.Table("playlist_tracks",
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.playlist_id')),
    db.Column('track_id', db.Integer, db.ForeignKey('tracks.track_id'))
)

class Playlist(db.Model):
    __tablename__ = "playlists"

    playlist_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable = False)
    owner_id = db.Column(db.Integer,db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String())
    collaborative = db.Column(db.Boolean(), nullable=False)
    public = db.Column(db.Boolean(), nullable=False)
    playlist_tracks = db.relationship('Track', secondary=playlist_tracks, backref=db.backref('playlist_tracks', lazy='dynamic'))