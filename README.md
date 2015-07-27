# Beeminder + Pomodoro = ❤️

Utilize the power of [Beeminder](http://beeminder.com/) and
[Pomodoro](http://pomodorotechnique.com). This little script runs a Pomodoro timer in your terminal
and increments your Beeminder goal counter when it's done.

## Quick start

1. Set the following environment variables (using `foreman`, `export`, ...):
  + `BEEMINDER_KEY` ... your Beeminder API key
  + `MASHAPE_KEY` ... your Mashape API consumer key
  + `BEEMINDER_USER` ... your Beeminder username
  + `BEEMINDER_GOAL` ... your Beeminder goal name (slug!)
2. `./beeminder.py "Work on secret project"`
3. ???
4. You just finished a Pomodoro

## Requirements

+ Python 3
+ OS X say (sry everyone else!)
