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

# @artists.route("/", methods=["POST"])
# def artist_create():
#     #Create a new artist
#     artist_fields = artist_schema.load(request.json)

#     new_artist = Artist()
#     new_artist.name = artist_fields["name"]
#     new_artist.uri = artist_fields["uri"]

#     db.session.add(new_artist)
#     db.session.commit()

#     return jsonify(artist_schema.dump(new_artist))

# @artists.route("/<int:id>", methods=["GET"])
# def artist_show(id):
#     #Return a single artist
#     artist = Artist.query.get(id)
#     return jsonify(artist_schema.dump(artist))

# @artists.route("/<int:id>", methods=["PUT", "PATCH"])
# def artist_update(id):
#     #Update an artist
#     artists = Artist.query.filter_by(id=id)
#     artist_fields = artist_schema.load(request.json)
#     artists.update(artist_fields)
#     db.session.commit()

#     return jsonify(artist_schema.dump(artists[0]))

# @artists.route("/<int:id>", methods=["DELETE"])
# def artist_delete(id):
#     artist = Artist.query.get(id)
    
#     if not artist:
#         return abort(404)
#     db.session.delete(artist)
#     db.session.commit()

#     return jsonify(artist_schema.dump(artist))