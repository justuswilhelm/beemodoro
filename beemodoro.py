#!/usr/bin/env python3
from multiprocessing import Process
from os import (
    environ,
    system,
)
from sys import argv
from requests import post
from time import sleep

POMODORO_LENGTH = 25 * 60
BREAK_LENGTH = 5 * 60
messages = {
    'POMODORO_START': 'Pomodoro has started',
    'POMODORO_OVER': 'Pomodoro Over',
    'BREAK_START': 'Start your break',
    'BREAK_OVER': 'Break Over',
}
BEEMINDER_KEY = environ['BEEMINDER_KEY']
MASHAPE_KEY = environ['MASHAPE_KEY']
USER = environ['BEEMINDER_USER']
GOAL = environ['BEEMINDER_GOAL']


def say_print(message_id):
    say = lambda: system("say {}".format(message))
    message = messages[message_id]
    print(message)
    p = Process(target=say)
    p.start()


def send_data(activity):
    post('https://dreeves-beeminder.p.mashape.com/users/{user}/goals/{goal}/'
         'datapoints.json?auth_token={beeminder_key}&username={user}'.format(
             user=USER, goal=GOAL, beeminder_key=BEEMINDER_KEY),
         headers={'X-Mashape-Key': MASHAPE_KEY},
         data={'comment': activity, 'value': '1', 'sendmail': 'false'})


def timer(length):
    for i in reversed(range(length)):
        minutes = i // 60
        seconds = i % 60
        print("\r", end='')
        print(
            "Time remaining: {:02}:{:02}".format(minutes, seconds),
            end='',
            flush=True)
        sleep(1)
    print("")


def pomodoro(activity, length=POMODORO_LENGTH):
    say_print('POMODORO_START')
    timer(length)
    say_print('POMODORO_OVER')

    send_data(activity)

    say_print('BREAK_START')
    timer(BREAK_LENGTH)
    say_print('BREAK_OVER')

if __name__ == "__main__":
    assert len(argv) >= 2
    msg = argv[1]
    if len(argv) == 3:
        length = int(argv[2]) * 60
    else:
        length = POMODORO_LENGTH

    pomodoro(msg, length=length)
