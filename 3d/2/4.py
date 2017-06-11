#!/usr/bin/env python
#-*-coding: utf-8-*-

# Version: 0.1
# Author: Song Huang <huangxiaohen2738@gmail.com>
# License: Copyright(c) 2015 Song.Huang
# Summary: 

import numpy as np

'''
def func(x, c, c0, hc):
    x = x - int(x)
    if x >= c: r= 0.0
    elif x<c0: r = x/c0 *hc
    else:
        r = ((c-x)/ (c-c0) )*hc

    return r
'''
def func(c, c0, hc):
    def trifunc(x):
        x = x - int(x)
        if x >= c: r= 0.0
        elif x<c0: r = x/c0 *hc
        else:
            r = ((c-x)/ (c-c0) )*hc
        return r

    return np.frompyfunc(trifunc, 1, 1)

x = np.linspace(0, 2, 100)
#funcs = np.frompyfunc(lambda x:func(x, 0.6, 0.4, 1.0), 1, 1)
#y = funcs(x)
y = func(0.6, 0.4, 1.0)(x)
print (y.astype(np.float64))
