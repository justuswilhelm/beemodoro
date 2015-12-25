#!/usr/bin/env python3
from argparse import ArgumentParser

from beemodoro import send_data


def main():
    parser = ArgumentParser(
        description="Transmit goal data to Beeminder")
    parser.add_argument(
        'activity', metavar='ACTIVITY', type=str, nargs=1,
        help='information about the activity that you performed'
    )
    args = parser.parse_args()
    send_data(args.activity)


if __name__ == "__main__":
    main()
