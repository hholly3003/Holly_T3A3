from models.Artist import Artist
from main import db
from flask import Blueprint, request, jsonify, abort
from schemas.ArtistSchema import artists_schema, artist_schema

artists = Blueprint("artists",__name__, url_prefix="/artists")

@artists.route("/", methods=["GET"])
def artists_index():
    #Return all artists
    artists = Artist.query.all()
    serialized_data = artists_schema.dump(artists)
    return jsonify(serialized_data)

# @artists.route("/", methods=["POST"])
# def playlist_create():
#     #Create a new playlist
#     playlist_fields = playlist_schema.load(request.json)

#     new_playlist = Playlist()
#     new_playlist.title = playlist_fields["title"]

#     db.session.add(new_playlist)
#     db.session.commit()

#     return jsonify(playlist_schema.dump(new_playlist))

# @artists.route("/<int:id>", methods=["GET"])
# def playlist_show(id):
#     #Return a single book
#     playlist = Playlist.query.get(id)
#     return jsonify(playlist_schema.dump(playlist))

# @artists.route("/<int:id>", methods=["PUT", "PATCH"])
# def playlist_update(id):
#     #Update a book
#     playlists = Playlist.query.filter_by(id=id)
#     playlist_fields = playlist_schema.load(request.json)
#     playlists.update(playlist_fields)
#     db.session.commit()

#     return jsonify(playlist_schema.dump(playlists[0]))

# @artists.route("/<int:id>", methods=["DELETE"])
# def playlist_delete(id):
#     playlist = Playlist.query.get(id)
    
#     if not playlist:
#         return abort(404)
#     db.session.delete(playlist)
#     db.session.commit()

#     return jsonify(playlist_schema.dump(playlist))