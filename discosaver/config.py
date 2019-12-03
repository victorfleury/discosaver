import os
import json


USERNAMES = ['hobbesfleurin']


def set_env_vars():
    """Setting up environment."""
    creds_path = '{0}/creds.json'.format(os.path.dirname(__file__))
    with open(creds_path, 'r') as creds:
        env_vars = json.load(creds)
        for var, value in env_vars.items():
            os.environ[var] = value
