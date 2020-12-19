from models.Artist import Artist
from main import db
from flask import Blueprint, request, jsonify, abort
from schemas.ArtistSchema import artists_schema, artist_schema

artists = Blueprint("artists",__name__, url_prefix="/artists")

@artists.route("/", methods=["GET"])
def artist_index():
    #Return all artists
    artists = Artist.query.all()
    return jsonify(artists_schema.dump(artists))

@artists.route("/<int:id>", methods=["GET"])
def artist_show(id):
    #Return a single artist
    artist = Artist.query.get(id)
    return jsonify(artist_schema.dump(artist))