from main import db
from flask import Blueprint, request, jsonify, abort
from models.Playlist import Playlist
from models.User import User
from schemas.PlaylistSchema import playlist_schema, playlists_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

playlists = Blueprint("playlists", __name__, url_prefix="/playlists")

@playlists.route("/", methods=["GET"])
def playlist_index():
    playlists = Playlist.query.all()
    return jsonify(playlists_schema.dump(playlists))

@playlists.route("/", methods=["POST"])
@jwt_required
def playlist_create():
    #Create a new playlist
    playlist_fields = playlist_schema.load(request.json)
    user_id = get_jwt_identity()
    print(user_id)

    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    new_playlist = Playlist()
    new_playlist.name = playlist_fields["name"]
    new_playlist.description = ""
    new_playlist.collaborative = False
    new_playlist.public = True
    
    user.playlists.append(new_playlist)

    db.session.commit()

    return jsonify(playlist_schema.dump(new_playlist))

@playlists.route("/<int:id>", methods=["GET"])
def playlist_show(id):
    #Return a single playlist
    playlist = Playlist.query.get(id)
    return jsonify(playlist_schema.dump(playlist))

@jwt_required
@playlists.route("/<int:id>", methods=["PUT", "PATCH"])
def playlist_update(id):
    #Update a book
    playlist_fields = playlist_schema.load(request.json)
    user_id = get_jwt_identity()

    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    playlists = Playlist.query.filter_by(id=id, user_id=user.id)

    if playlists.count() != 1:
        return abort(401, description="Unauthorised to update this book")
    
    playlists.update(playlist_fields)
    db.session.commit()

    return jsonify(playlist_schema.dump(playlists[0]))

@jwt_required
@playlists.route("/<int:id>", methods=["DELETE"])
def playlist_delete(id):
    user_id = get_jwt_identity()

    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    playlist = Playlist.query.filter_by(id=id, user_id=user.id).first()

    if not playlist:
        return abort(400)

    db.session.delete(playlist)
    db.session.commit()

    return jsonify(playlist_schema.dump(playlist))