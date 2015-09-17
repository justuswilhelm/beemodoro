#!/usr/bin/env python3
from sys import argv

from beemodoro.beemodoro import send_data

def main():
    goal = argv[1]
    activity = argv[2]

    send_data(activity, goal=goal)


if __name__ == "__main__":
    main()
