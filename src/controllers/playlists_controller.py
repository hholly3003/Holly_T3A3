from main import db
from flask import Blueprint, request, jsonify, abort
from models.Playlist import Playlist
from models.User import User
from schemas.PlaylistSchema import playlist_schema, playlists_schema
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload
from flask_jwt_extended import jwt_required, get_jwt_identity

playlists = Blueprint("playlists", __name__, url_prefix="/playlists")

@playlists.route("/", methods=["GET"])
def playlist_index():
    playlists = Playlist.query.option(joinedload("user")).all()
    return jsonify(playlists_schema.dump(playlists))

@playlists.route("/", methods=["POST"])
@jwt_required
@verify_user
def playlist_create(user=None):
    #Create a new playlist
    playlist_fields = playlist_schema.load(request.json)
    user_id = get_jwt_identity()
    
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

@playlists.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
@verify_user
def playlist_update(id, user=None):
    #Update a book
    playlist_fields = playlist_schema.load(request.json)
    user_id = get_jwt_identity()
    
    playlists = Playlist.query.filter_by(playlist_id=id, owner_id=user.id)
    if playlists.count() != 1:
        return abort(401, description="Unauthorised to update this book")
    
    playlists.update(playlist_fields)
    db.session.commit()

    return jsonify(playlist_schema.dump(playlists[0]))

@playlists.route("/<int:id>", methods=["DELETE"])
@jwt_required
@verify_user
def playlist_delete(id, user=None):
    user_id = get_jwt_identity()

    playlist = Playlist.query.filter_by(playlist_id=id, owner_id=user.id).first()
    if not playlist:
        return abort(400)

    db.session.delete(playlist)
    db.session.commit()

    return jsonify(playlist_schema.dump(playlist))