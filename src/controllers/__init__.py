from controllers.users_controller import users
from controllers.artists_contoller import artists
from controllers.albums_controller import albums
from controllers.collections_controller import collections
from controllers.playlists_controller import playlists
from controllers.profiles_controller import profiles
from controllers.tracks_controller import tracks



registerable_controllers = [
    users,
    artists,
    albums,
    collections,
    playlists,
    profiles,
    tracks
]