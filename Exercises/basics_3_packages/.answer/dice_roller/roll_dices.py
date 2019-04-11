#!/usr/bin/env python
""" 
This module contains a function that simulates a six side dice roll
"""  

import dice_roller.dices as dices


def main():
    
    while True:
        
        n_sides = input('Enter the number of sides the dice will have or type "q" to quit: ')

        if n_sides == '6':
            dice = dices.Dice()

        elif n_sides == '4':
            dice = dices.FourSidedDice()

        elif n_sides == '8':
            dice = dices.EightSidedDice()

        elif n_sides == 'q':
            print('Leaving')
            break

        else:
            continue
        
        print('The {}-sided dice gave me {}'.format(dice.sides, roll(dice)))


def roll(dice):
    return dice.roll()


if __name__ == '__main__':
    main()
