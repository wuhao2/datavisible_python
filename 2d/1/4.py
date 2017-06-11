#!/usr/bin/env python
#-*-coding: utf-8-*-

# Version: 0.1
# Author: Song Huang <huangxiaohen2738@gmail.com>
# License: Copyright(c) 2015 Song.Huang
# Summary: 

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("1.txt")
width = (data[1,0] - data[0, 0])*0.4

plt.figure(figsize=(8, 5))
plt.bar(data[:, 0]-width, data[:, 1], width, label='Person')
plt.xlim(-width, 40)
plt.xlabel("Age")
plt.ylabel("Num")
plt.legend()
plt.show()
