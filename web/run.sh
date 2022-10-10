#!/bin/bash

export FLASK_APP=/home/pi/Code/rpi-sleeptrainer/web/sleeptrainer-web.py
/usr/bin/python -m flask run --host=0.0.0.0

