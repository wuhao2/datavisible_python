#!/usr/bin/env python
#-*-coding: utf-8-*-

# Version: 0.1
# Author: Song Huang <huangxiaohen2738@gmail.com>
# License: Copyright(c) 2015 Song.Huang
# Summary: ethon.sinaapp.com

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def randrange(n, vmin, vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = randrange(100, 0, 100)
    ys = randrange(100, 0, 100)
    zs = randrange(100, zl, zh)

    ax.scatter(xs, ys ,zs, c=c, marker=m)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()


