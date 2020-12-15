from main import db
from models.Playlist import Playlist

collection_playlists = db.Table("collection_playlists",
    db.Column('collection_id', db.Integer, db.ForeignKey('colections.id'))
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.id'))
)

class Collection(db.Model):
    __tablename__ = "collections"

    collection_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable = False)
    owner_id = db.Column(db.Integer,db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String())
    collaborative = db.Column(db.Boolean(), nullable=False)
    public = db.Column(db.Boolean(), nullable=False)
    collection_playlists = db.relationship('Playlist', secondary=collection_playlists, backref=db.backref('collection_playlists', lazy='dynamic'))