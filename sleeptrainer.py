#!/usr/bin/env python

import sys

from sense_hat import SenseHat

colors = {
        'black'  : (0, 0, 0),
        'grey'   : (128, 128, 128),
        'red'    : (255, 0, 0),
        'blue'   : (0, 0, 255),
        'green'  : (0, 255, 0),
        'yellow' : (255, 255, 0),
        'orange' : (255, 165, 0),
        'white'  : (255, 255, 255)
        }

color_name = sys.argv[1] if len(sys.argv) > 1 else 'black'
low_light = (sys.argv[2] == 'True') if len(sys.argv) > 2 else True

color = colors[color_name] if color_name in colors else colors['black']
k = colors['black']

print ('Setting color to: ', color_name, '(',  color, '), low_light = ', low_light)

sense = SenseHat()
sense.low_light = low_light
#sense.low_light = True
#sense.low_light = False
# sense.clear(g)
# sense.clear(y)

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

sense.set_pixels(draw_circle(color))

