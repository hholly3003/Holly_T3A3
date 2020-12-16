from main import db
from flask import Blueprint, request, jsonify
from models.Playlist import Playlist
from schemas.PlaylistSchema import playlist_schema, playlists_schema
# from flask_jwt_extended import jwt_required

playlists = Blueprint("playlists", __name__, url_prefix="/playlists")

@playlists.route("/", methods=["GET"])
def playlist_index():
    playlists = Playlist.query.all()
    return jsonify(playlists_schemas.dump(playlists))

@playlists.route("/", methods=["POST"])
def playlist_create():
    #Create a new playlist
    playlist_fields = playlist_schema.load(request.json)

    new_playlist = Playlist()
    new_playlist.title = playlist_fields["title"]

    db.session.add(new_playlist)
    db.session.commit()

    return jsonify(playlist_schema.dump(new_playlist))

@playlists.route("/<int:id>", methods=["GET"])
def playlist_show(id):
    #Return a single book
    playlist = Playlist.query.get(id)
    return jsonify(playlist_schema.dump(playlist))

@playlists.route("/<int:id>", methods=["PUT", "PATCH"])
def playlist_update(id):
    #Update a book
    playlists = Playlist.query.filter_by(id=id)
    playlist_fields = playlist_schema.load(request.json)
    playlists.update(playlist_fields)
    db.session.commit()

    return jsonify(playlist_schema.dump(playlists[0]))

@playlists.route("/<int:id>", methods=["DELETE"])
def playlist_delete(id):
    playlist = Playlist.query.get(id)

    db.session.delete(playlist)
    db.session.commit()

    return jsonify(playlist_schema.dump(playlist))