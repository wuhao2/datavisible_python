#!/usr/bin/env python
#-*-coding: utf-8-*-

# Version: 0.1
# Author: Song Huang <huangxiaohen2738@gmail.com>
# License: Copyright(c) 2015 Song.Huang
# Summary: 

import matplotlib.pyplot as plt

for idx, color in enumerate("rgbyck"):
    plt.subplot(320+idx+1, axisbg=color)

plt.show()
