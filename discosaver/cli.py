"""Console script for discosaver."""
import argparse
import sys

from . import discosaver


def main():
    """Console script for discosaver."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--id',
        help='Show the id of the playlist',
        action='store_true'
    )
    parser.add_argument(
        '--create',
        help='Create the playlist',
        action='store_true'
    )
    parser.add_argument(
        '--get_tracks_ids',
        help='Get the tracks ids',
        action='store_true'
    )
    args = parser.parse_args()

    if args.id:
        print('Getting the playlist id...')
        print(discosaver.get_discover_weekly_id())
        return 0
    if args.create:
        print('Creating playlist...')
        discosaver.create_playlist()
        return 0
    if args.get_tracks_ids:
        print('Getting tracks ids...')
        discosaver.get_tracks_ids()
        return 0

    print('Saving playlist...')
    discosaver.discosave()

    return 0


if __name__ == "__main__":
    sys.exit(main())
