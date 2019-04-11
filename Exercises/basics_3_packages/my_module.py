#!/usr/bin/env python
""" 
This module contains a function that simulates a six side dice roll
"""  

import random

def roll_dice():
    _min = 1
    _max = 6
    result = random.randint(_min, _max)
    return result

print('The dice gave me {}'.format(roll_dice()))

