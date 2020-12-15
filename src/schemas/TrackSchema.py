from main import ma
from models.Track import Track
from marshmallow.validate import Length

class TrackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Track
    
    name = ma.String(required=True, validate=Length(min=1))
    track_num = ma.Integer(required=True)
    disc_num = ma.Integer(required=True)
    duration_ms = ma.Integer(required=True)
    explicit = ma.Boolean(required=True)
    
track_schema = TrackSchema()
tracks_schema = TrackSchema(many=True)