#!/usr/bin/env python
#-*-coding: utf-8-*-

# Version: 0.1
# Author: Song Huang <huangxiaohen2738@gmail.com>
# License: Copyright(c) 2015 Song.Huang
# Summary: 

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4))
x = np.random.random(100)
y = np.random.random(100)

plt.scatter(x, y, s=x*1000, c=y, marker = (5,1), alpha=0.8, lw=2, facecolor="none")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()
