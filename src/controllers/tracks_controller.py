from main import db
from flask import Blueprint, request, jsonify
from models.Track import Track
from schemas.TrackSchema import track_schema, tracks_schema
from sqlalchemy.orm import joinedload

tracks = Blueprint("tracks", __name__, url_prefix="/tracks")

@tracks.route("/", methods=["GET"])
def track_index():
    tracks = Track.query.options(joinedload("album")).all()
    return jsonify(tracks_schema.dump(tracks))

@tracks.route("/", methods=["POST"])
def track_create(user):
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