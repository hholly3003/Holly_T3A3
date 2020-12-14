from main import ma
from models.Artist import Artist
from marshmallow.validate import Length

class ArtistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Artist
    
    name = ma.String(required=True, validate=Length(min=1))

artist_schema = ArtistSchema()
artists_schema = ArtistSchema(many=True)