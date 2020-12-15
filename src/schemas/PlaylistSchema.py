from main import ma
from models.Playlist import Playlist
from marshmallow.validate import Length

class PlaylistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Playlist
    
    name = ma.String(required=True, validate=Length(min=1))
    collaborative = ma.Boolean(required=True)
    public = ma.Boolean(required=True)
    
playlist_schema = PlaylistSchema()
playlists_schema = PlaylistSchema(many=True)