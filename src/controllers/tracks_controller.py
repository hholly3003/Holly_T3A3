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

@tracks.route("/<int:id>", methods=["GET"])
def track_show(id):
    #Return a single track
    track = Track.query.get(id)
    return jsonify(track_schema.dump(track))