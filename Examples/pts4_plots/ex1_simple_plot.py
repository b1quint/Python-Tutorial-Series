#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Python Tutorial Series #4 - Example 1: A Simple Plot

    Exercise: 
        1. Change the code to avoid the "from matplotlib.pyplot import *".
        2. Add labels to the X and Y axis.
        3. Add a grid.
        4. Add a title.
        5. Save the figure into the "ex1_simple_plot.png" file.
"""

from matplotlib.pyplot import *

x = [0, 1, 2, 3, 4]
y = [4, 1, 0, 1, 4]

plot(x, y)
xlabel(r"$\alpha$")
show()
