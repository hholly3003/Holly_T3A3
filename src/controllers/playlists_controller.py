from main import db
from flask import Blueprint, request, jsonify
from models.Playlist import Playlist
from schemas.PlaylistSchema import playlist_schema, playlists_schema

playlists = Blueprint("playlists", __name__, url_prefix="/playlists")

@playlists.route("/", methods=["GET"])
def playlist_index():
    playlists = Playlist.query.all()
    return jsonify(playlists_schemas.dump(playlists))