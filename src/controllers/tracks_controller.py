from main import db
from flask import Blueprint, request, jsonify
from models.Track import Track
from schemas.TrackSchema import track_schema, tracks_schema
from sqlalchemy.orm import joinedload
from flask_jwt_extended import jwt_required

tracks = Blueprint("tracks", __name__, url_prefix="/tracks")

@tracks.route("/", methods=["GET"])
def track_index():
    tracks = Track.query.options(joinedload("album")).all()
    return jsonify(tracks_schema.dump(tracks))

@jwt_required
@tracks.route("/", methods=["POST"])
def track_create():
    track_fields = track_schema.load(request.json)

    new_track = Track()
    new_track.name = track_fields["name"]
    new_track.track_num = track_fields["track_num"]
    new_track.disc_num = track_fields["disc_num"]
    new_track.duration_ms = track_fields["duration_ms"]
    new_track.explicit = track_fields["explicit"]

    album.tracks.append(new_track)

    db.session.commit()

    return jsonify(track_schema.dump(new_track))

@tracks.route("/<int:id>", methods=["GET"])
def track_show(id):
    #Return a single track
    track = Track.query.get(id)
    return jsonify(track_schema.dump(track))

# @tracks.route("/<int:id>", methods=["PUT", "PATCH"])
# @jwt_required
# def track_update(id):
#     #Update to love a track
#     track_fields = track_schema.load(request.json)
    
#     playlists = Playlist.query.filter_by(playlist_id=id, owner_id=user.id)
#     if playlists.count() != 1:
#         return abort(401, description="Unauthorised to update this book")
    
#     playlists.update(playlist_fields)
#     db.session.commit()

#     return jsonify(playlist_schema.dump(playlists[0]))
