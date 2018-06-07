#!/usr/bin/env python
# -*- coding: utf-8 -+-
"""
    Python Tutorial Series #4 - Example 3: Figures and Axes
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5) - 2
y = x ** 2

#fig = plt.figure(num="My_Figure")
fig, axes = plt.subplots(2, 2, num="My_Figure")
#ax1 = fig.add_subplot(211)
#ax2 = fig.add_subplot(223)
#ax3 = fig.add_subplot(4,4,15)
ax1 = axes[0,1]
ax2 = axes[1,0]
ax3 = axes[1,1]

ax1.plot(x, y, "C0o")
ax1.set_xlim(-3, 3)
ax1.set_ylim(-1, 5)
ax1.set_title("Axis 1 (211)")

ax2.plot(x, y, "C1s")
ax2.set_title("Axis 2 (223)")

ax3.plot(x, y, "C2:")
ax3.set_title("Axis 3 (224)")

fig.tight_layout()
plt.show()

