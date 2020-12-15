from main import ma
from models.Collection import Collection
from marshmallow.validate import Length

class CollectionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Collection
    
    name = ma.String(required=True, validate=Length(min=1))
    collaborative = ma.Boolean(required=True)
    public = ma.Boolean(required=True)
    
collection_schema = CollectionSchema()
collections_schema = CollectionSchema(many=True)