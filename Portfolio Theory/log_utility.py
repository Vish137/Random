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
    0. W (initial wealth), default=1
    1. res (grid resolution), default=100
    2. a (Bernoulli parameter), default=0
    3. b (Bernoulli parameter), default=1

-------
OUTPUTS
-------
1. v - List of values for the utility function at each wealth

"""
import numpy as np
def log_utility(x_lower,x_upper,*args):
    if args:
        if len(args)<4:
            raise ValueError('You must specify W, res, a, and b, in that order')
        x = np.linspace(x_lower,x_upper,args[1])
        v=[]
        for _ in range(x_lower,x_upper):
            v.append(args[3]*np.log( 1 + x[_]/args[0]) + args[2])
    else: 
        x = np.linspace(x_lower,x_upper,100)
        v=[]
        for _ in range(x_lower,x_upper):
            v.append(np.log(1 + x))
    return v

