# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 23:08:28 2021

@author: Vish137

Description: stores a 1-dim log utility function as a list

------
INPUTS
------
x_lower - lower bound
x_upper - upper bound
args:
    W (initial wealth), default=0
    res (grid resolution), default=100
"""
import numpy as np
def log_utility(x_lower,x_upper,*args):
    if args:
        if len(args)<2:
            raise ValueError('You must specify W and res, in that order')
        x = np.linspace(x_lower,x_upper,args[1])
        f = np.log(x+args[0])
        v=[]
        for _ in range(1,x_upper):
            v.append(np.log( 1 + x[_]/args[0]))
    else: 
        x = np.linspace(x_lower,x_upper,100)
        f = np.log(x+0)
        v=[]
        for _ in range(x_lower,x_upper):
            v.append(np.log(1 + x))
    return v

