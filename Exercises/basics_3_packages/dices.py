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
    ----------
    _min : int
        Minimum possible value to be returned
    _max : int
        Maximum possible value to be returned
    """

    _min = 1
    _max = 6

    def roll(self):
        """Returns a random integer number between `_min` and `_max`"""
        return random.randint(self._min, self._max)


class FourSidedDice(Dice):
    """A four sided dice."""

    def __init__(self)
        self._max = 4


class EightSidedDice(Dice):
    """An eight sided dice."""

    def __init__(self)
        self._max = 8


