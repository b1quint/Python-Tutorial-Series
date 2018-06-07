#!/usr/bin/env python
# -*- coding: utf-8 -+-
"""
    Python Tutorial Series #4 - Example 4: Plots with Style
"""

import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return (t - 2.) ** 2.

t1 = np.arange(0.0, 5.0, 0.5)
t2 = np.arange(0.0, 5.0, 0.02)

print(plt.style.available)
plt.style.use("grayscale")

plt.plot(t2, f(t2), 'C0-', label="lines")
plt.plot(t1, f(t1), 'C1o', label="circles")

plt.title("A simple plot")

plt.grid()
plt.legend()
plt.tight_layout()

plt.savefig('fig_ex4c.png')
