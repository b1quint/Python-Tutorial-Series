#!/usr/bin/env python
# -*- coding: utf-8 -+-
"""
    Python Tutorial Series #4 - Example 3: Figures and Axes
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5) - 2
y = x ** 2

fig = plt.figure(num="My_Figure")
ax = fig.add_subplot(111)

ax.plot(x, y, "o")
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 5)

plt.show()

