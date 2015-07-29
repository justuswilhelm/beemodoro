#!/usr/bin/env python3
from sys import argv

from beemodoro import send_data

goal = argv[1]
activity = argv[2]

print(send_data(activity, goal=goal))
