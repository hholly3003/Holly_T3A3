from models.Album import Album
from main import db
from flask import Blueprint, request, jsonify, abort
from schemas.AlbumSchema import album_schema, albums_schema

albums = Blueprint("albums", __name__, url_prefix="/albums")

@albums.route("/", methods=["GET"])
def album_index():
    #Return all albums
    albums = Album.query.all()
    print(albums[0].album_type, "******************************")
    return jsonify(albums_schema.dump(albums))

@albums.route("/<int:id>", methods=["GET"])
def album_show(id):
    album = Album.query.get(id)
    return jsonify(album_schema.dump(album))