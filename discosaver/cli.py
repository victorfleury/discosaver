"""Console script for discosaver."""
import argparse
import sys

import discosaver


def main():
    """Console script for discosaver."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--id',
        help='Show the id of the playlist',
        action='store_true'
    )
    args = parser.parse_args()

    if args.id:
        print('Getting the playlist id...')
        print(discosaver.get_discover_weekly_id())
    return 0


if __name__ == "__main__":
    sys.exit(main())
