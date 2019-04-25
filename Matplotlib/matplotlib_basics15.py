# Topic: Creating Scatter Plots

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(200)
y = np.random.randn(200)
size = 50*np.random.rand(200)
# print(size)
colors = np.random.rand(200)
# print(colors)

plt.scatter(x, y, s=size, c=colors, marker="_")
plt.show()

# Some of the markers are:
#
# + - Plus Marker
# _ - Underscore/Dash Marker
# * - Star Marker
# . - Small Circle Marker
# o - Large Circle Marker
# , - Square Marker
# s - Square Marker
# ^ - Triangle Marker
# v - Reverse Triangle Marker
# x - Simple X Marker
# X - Bold X Marker
