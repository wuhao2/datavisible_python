#!/usr/bin/env python
#-*-coding: utf-8-*-

# Version: 0.1
# Author: Song Huang <huangxiaohen2738@gmail.com>
# License: Copyright(c) 2015 Song.Huang
# Summary: ethon.sinaapp.com

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x)

plt.figure(figsize=(8, 4))
plt.plot(x,y,color = 'red', label='$sin(x)$')
plt.plot(x,z,"b--",label='$cos(x)$')
plt.xlabel(("Time(s)"))
plt.ylabel("")
plt.title("matplotlib")
plt.ylim(-1.2, 1.2)
plt.legend()
plt.show()

fig = plt.gcf()
ax = plt.gca()
print (fig)
print (ax)
