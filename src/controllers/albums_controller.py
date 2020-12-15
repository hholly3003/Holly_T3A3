from models.Album import Album
from main import db
from flask import Blueprint, request, jsonify, abort
from schemas.AlbumSchema import album_schema, albums_schema

albums = Blueprint("albums", __name__, url_prefix="/albums")

@albums.route("/", methods=["GET"])
def album_index():
    #Return all albums
    albums = Album.query.all()
    return jsonify(albums_schema.dump(albums))

@albums.route("/<int:id>", methods=["GET"])
def album_show(id):
    album = Album.query.get(id)
    return jsonify(album_schema.dump(album))

# @albums.route("/", methods=["POST"])
# def album_create():
#     #Create a new album
#     album_fields = album_schema.load(request.json)

#     new_album = Album()
#     new_album.name = album_fields["name"]
#     new_album.album_type = album_fields["album_type"]

#     db.session.add(new_album)
#     db.session.commit()

#     return jsonify(album_schema.dump(new_album))

# @albums.route("/<int:id>", methods=["PUT", "PATCH"])
# def album_update(id):
#     albums = Album.query.filter_by(id=id)
#     album_fields = album_schema.load(request.json)
#     albums.update(album_fields)
#     db.session.commit()

#     return jsonify(album_schema.dump(albums[0]))

# @albums.route("/<int:id>", methods=["DELETE"])
# def album_delete(id):
#     album = Album.query.get(id)

#     if not album:
#         return abort(404)
#     db.session.delete(album)
#     db.session.commit()

#     return jsonify(album_schema.dump(album))