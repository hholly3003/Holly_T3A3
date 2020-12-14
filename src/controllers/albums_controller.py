from models.Album import Album
from main import db
from flask import Blueprint, request, jsonify, abort
from schemas.AlbumSchema import album_schema, albums_schema

albums = Blueprint("albums", __name__, url_prefix="/albums")

@albums.route("/", methods=["GET"])
def album_index():
    #Return all albums
    albums = Album.query.all()
    serialised_data = albums_schema.dump(albums)
    return jsonify(serialised_data)