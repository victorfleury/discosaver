"""Main module."""
import datetime
from pprint import pprint
import time

import spotipy
import spotipy.util as util

from . import config

config.set_env_vars()
username = next(iter(config.USERNAMES))


def get_discover_weekly_id():
    """Get the discover weekly."""
    scope = 'playlist-read-private'
    token = util.prompt_for_user_token(
        username,
        scope,
        local_webserver=True,
    )
    if not token:
        raise ValueError('Could not get a valid token.')
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['name'] == 'Discover Weekly':
            return playlist['id']


def create_playlist():
    """Create the playlist to save the discover weekly."""
    token = util.prompt_for_user_token(
        username,
        scope='playlist-modify-private',
        local_webserver=True,
    )
    if not token:
        raise ValueError('Token not found')
    sp = spotipy.Spotify(auth=token)
    sp.trace = True
    playlists = sp.user_playlist_create(
        username,
        _playlist_name(),
        '')
    if playlists:
        print('Playlist created as', _playlist_name())
        return playlists.get('id')


def _playlist_name():
    """Generate a playlist name

    Returns:
        str: The playlist name.
    """
    date = datetime.datetime.now()
    year, month, day = (date.year, date.month, date.day)
    week = datetime.date(year, month, day).isocalendar()[1]
    return f'Saved Discover Weekly #{week}'


def get_tracks_ids(playlist_id=None):
    """Get the tracks ids.

    Returns:
        list([str]): A list of ids
    """
    playlist_id = playlist_id or get_discover_weekly_id()

    token = util.prompt_for_user_token(username, local_webserver=True)
    sp = spotipy.Spotify(auth=token)

    playlist_discover_weekly = sp.user_playlist(
        username,
        playlist_id,
        fields="tracks,next",
    )
    tracks_ids = [
        track.get('track').get('id')
        for track in playlist_discover_weekly['tracks']['items']
    ]
    return tracks_ids


def add_tracks_to_playlist(playlist_id, track_ids):
    """Add tracks to a playlist

    Args:
        playlist_id (str): A playlist id
        track_ids (list[str]): A list of ids
    """
    scope = 'playlist-modify-private'
    token = util.prompt_for_user_token(username, scope, local_webserver=True)

    if not token:
        raise ValueError('Could not find token...')

    sp = spotipy.Spotify(auth=token)
    sp.trace = True
    pprint(track_ids)
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)

    if results:
        print('Adding tracks successful.')
    else:
        print('Something went wrong...')


def discosave():
    """Where the magic happens."""

    # Create destination playlist
    print('Creating destination playlist')
    dest_id = create_playlist()

    time.sleep(5)

    # Get The discover weekly id
    print('Getting id')
    source_id = get_discover_weekly_id()

    time.sleep(1)

    # Get tracks ids
    print('Getting tracks id')
    tracks_ids = get_tracks_ids(source_id)

    time.sleep(5)

    # Add tracks
    add_tracks_to_playlist(dest_id, tracks_ids)
    print('Done')
