#!/usr/bin/env python

import sys

from flask import Flask
from flask import redirect, render_template, request, url_for
from sense_hat import SenseHat

COLORS = {
        'black'  : (0, 0, 0),
        'grey'   : (128, 128, 128),
        'red'    : (255, 0, 0),
        'blue'   : (0, 0, 255),
        'green'  : (0, 255, 0),
        'yellow' : (255, 255, 0),
        'orange' : (255, 165, 0),
        'white'  : (255, 255, 255)
        }

k = COLORS['black'] 

def draw_circle(x):
    return [
            k, k, k, k, k, k, k, k,
            k, k, k, k, k, k, k, k,
            k, k, k, x, x, k, k, k,
            k, k, x, x, x, x, k, k,
            k, k, x, x, x, x, k, k,
            k, k, k, x, x, k, k, k,
            k, k, k, k, k, k, k, k,
            k, k, k, k, k, k, k, k
        ]

app = Flask(__name__)
sense = SenseHat()

@app.route("/")
@app.route("/index.html")
def index():
    currentColor = sense.get_pixel(4, 4)
    return render_template('index.html', currentColor=currentColor)

@app.route("/setLedColor", methods=['POST'])
def setLedColor():
    color = request.form['color']
    sense.low_light = True
    sense.set_pixels(draw_circle(COLORS[color]))  
    return redirect(url_for('index'))

@app.route("/leds/<color>")
def leds_green(color):
    sense.low_light = True
    sense.set_pixels(draw_circle(COLORS[color]))   
    return "Color set to: " + color +  "\n"

