#!/usr/bin/env python
""" 
This module contains a function that simulates a six side dice roll
"""  

import dice_roller.dices as dices


def main():
    
    print('The dice gave me {}'.format(roll()))


def roll():

    dice = dices.Dice()
    result = dice.roll()
    
    return result


if __name__ == '__main__':
    main()
