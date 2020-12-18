from main import ma
from models.AlbumType import AlbumType
from marshmallow.validate import Length

class AlbumTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AlbumType

    name = ma.String(required=True, validate=Length(min=1))

album_type_schema = AlbumTypeSchema()