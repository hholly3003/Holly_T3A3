from main import db

class Playlist(db.Model):
    __tablename__ = "playlists"

    playlist_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable = False)
    owner_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    description = db.Column(db.String())
    collaborative = db.Column(db.Boolean())
    public = db.Column(db.Boolean())