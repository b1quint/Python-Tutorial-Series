#!/usr/bin/env python
"""
This file is part of the Python Tutorial Series 2019 by Bruno C. Quint.

It contains classes that will be used on the third edition of the PTS2019.
"""

import random


class Dice:
    """
    A basic Dice is a Dice with six sides.

    Attributes
    sides : int
        Maximum possible value to be returned
    """
    sides = 6

    def roll(self):
        """Returns a random integer number between `_min` and `_max`"""
        return random.randint(1, self.sides)


class FourSidedDice(Dice):
    """A four sided dice."""

    def __init__(self):
        self.sides = 4


class EightSidedDice(Dice):
    """An eight sided dice."""

    def __init__(self):
        self.sides = 8


