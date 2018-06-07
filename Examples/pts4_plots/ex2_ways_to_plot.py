#!/usr/bin/env python
# -*- coding: utf-8 -+-
"""
    Python Tutorial Series #4 - Example 2: A Simple Plot
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.size'] = 18

def f(t):
    return (t - 2.) ** 2.

t1 = np.arange(0.0, 5.0, 0.5)
t2 = np.arange(0.0, 5.0, 0.02)

plt.plot(t2, f(t2), 'k-', label="lines")
plt.plot(t1, f(t1), 'ro', label="circles")

plt.xlabel('t [s]')
plt.ylabel(u"f(t) = (t - 2)$^2$") 

plt.title("A simple plot")

plt.grid()
plt.legend()
plt.tight_layout()

plt.savefig('ex2_fig5e.png')
