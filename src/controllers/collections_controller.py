from main import db
from flask import Blueprint, request, jsonify, abort, render_template
from models.Collection import Collection
from models.User import User
from schemas.CollectionSchema import collection_schema, collections_schema
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload
from flask_jwt_extended import jwt_required, get_jwt_identity

collections = Blueprint("collections", __name__, url_prefix="/collections")

@collections.route("/", methods=["GET"])
def collection_index():
    collections = Collection.query.options(joinedload("owner")).all()
    #return jsonify(collections_schema.dump(collections))
    return render_template("collections.html", collections=collections)

@collections.route("/", methods=["POST"])
@jwt_required
@verify_user
def collection_create(user=None):
    #Create a new collection
    collection_fields = collection_schema.load(request.json)
    
    new_collection = Collection()
    new_collection.name = collection_fields["name"]
    new_collection.description = collection_fields["description"]
    new_collection.collaborative = collection_fields["collaborative"]
    new_collection.public = collection_fields["public"]
    
    user.collections.append(new_collection)

    db.session.commit()

    return jsonify(collection_schema.dump(new_collection))

@collections.route("/<int:id>", methods=["GET"])
def collection_show(id):
    #Return a single playlist
    collection = Collection.query.get(id)
    return jsonify(collection_schema.dump(collection))

@collections.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
@verify_user
def collection_update(id, user=None):
    #Update a book
    collection_fields = collection_schema.load(request.json)
    
    collections = Collection.query.filter_by(collection_id=id, owner_id=user.id)
    if collections.count() != 1:
        return abort(401, description="Unauthorised to update this book")
    
    collections.update(collection_fields)
    db.session.commit()

    return jsonify(collection_schema.dump(collections[0]))

@collections.route("/<int:id>", methods=["DELETE"])
@jwt_required
@verify_user
def collection_delete(id, user=None):
    collection = Collection.query.filter_by(collection_id=id, owner_id=user.id).first()
    if not collection:
        return abort(400)

    db.session.delete(collection)
    db.session.commit()

    return jsonify(collection_schema.dump(collection))

@collections.route("/count", methods=["GET"])
@jwt_required
@verify_user
def collection_count(user=None):
    if user.is_admin == False:
        return abort(401, description="Unauthorised to this feature")

    query = db.session.query(Collection)

    count = query.count()
    return jsonify(count)