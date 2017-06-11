#!/usr/bin/env python
#-*-coding: utf-8-*-

# Version: 0.1
# Author: Song Huang <huangxiaohen2738@gmail.com>
# License: Copyright(c) 2015 Song.Huang
# Summary: ethon.sinaapp.com

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for c, z in zip(['r', 'g', 'b', 'y'], [30, 20, 10 ,0]):
    x = np.arange(20)
    y = np.random.rand(20)

    cs = [c] * len(x)
    cs[0] = 'c'
    ax.bar(x,y, zs=z, zdir='y', color=cs)
    #ax.set_xlabel
plt.show()
