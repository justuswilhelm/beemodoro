Beeminder + Pomodoro = 🍅
=========================
Utilize the power of `Beeminder <http://beeminder.com/>`_ and `Pomodoro
<http://pomodorotechnique.com>`_. This little script runs a Pomodoro timer in
your terminal and increments your Beeminder goal counter when it's done. This
requires your project to count 1 Pomodoro per step.

Quick start
-----------
1. Set the following environment variables (using ``foreman``, ``export``, ...):

  - ``BEEMINDER_KEY``: your Beeminder API key
  - ``BEEMINDER_USER``: your Beeminder username
  - ``BEEMINDER_GOAL``: your Beeminder goal slug name (can be found in your
    goal settings)

2. Run ``beemodoro "Work on secret project" [optional_custom_pomodoro_length]``
3. Work for 25 minutes
4. You just finished a Pomodoro! Yay! Take a break 🍅

Requirements
---------------
- Python 3
- OS X say (for TTS output)
