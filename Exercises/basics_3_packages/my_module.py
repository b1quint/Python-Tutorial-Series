#!/usr/bin/env python
""" 
This module, called my_module.py, contains a function that simulates a six side dice roll
"""  

import random

def roll_dice():
    _min = 1
    _max = 6
    result = random.randint(_min, _max)
    return result

print('Current scope: {}'.format(__name__))
print('The dice gave me {}'.format(roll_dice()))

