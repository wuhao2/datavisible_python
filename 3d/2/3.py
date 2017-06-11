#!/usr/bin/env python
#-*-coding: utf-8-*-

# Version: 0.1
# Author: Song Huang <huangxiaohen2738@gmail.com>
# License: Copyright(c) 2015 Song.Huang
# Summary: ethon.sinaapp.com

from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y, z = axes3d.get_test_data(0.05)

cset = ax.contour(x,y,z, extend3d=True, cmap = cm.coolwarm)
ax.clabel(cset, fontsize=9, inline=1)
plt.show()
