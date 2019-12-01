import os


USERNAMES = ['hobbesfleurin']
ENV = {
    'SPOTIPY_CLIENT_ID': '6820eac775304bfc98745e7ad8803880',
    'SPOTIPY_CLIENT_SECRET': '5ee18d751e55445b8287c289b3071093',
    'SPOTIPY_REDIRECT_URI': 'http://localhost:8080/',
}


def set_env_vars():
    """Setting up environment."""
    for var, value in ENV.items():
        os.environ[var] = value
