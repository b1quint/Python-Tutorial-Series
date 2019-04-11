#!/usr/bin/env python
""" 
This module contains a function that simulates a six side dice roll
"""  

import random


def roll():

    result = random.randint(1, 6)    
    
    return result


print('The dice gave me {}'.format(roll()))

