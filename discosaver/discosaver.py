"""Main module."""
import datetime

import spotipy
import spotipy.util as util

username = 'hobbesfleurin'


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
    token = util.prompt_for_user_token(username)
    if not token:
        raise ValueError
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlists = sp.user_playlist_create(
        username,
        ,
        playlist_description)

def _playlist_name():
    return f'Saved Discover Weekly #{datetime.}'