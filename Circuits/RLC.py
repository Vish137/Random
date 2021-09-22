# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 01:37:07 2021

@author: Vish137

Description: Solving for the voltage across a connected capaitor in an RLC loop via Euler method

------
INPUTS
------
V0 - Input voltage/emf (Volts)
L - inductance (Henry)
C - capacitance (Farad) 
R - resistance (Ohm)
T - total display time
dt - time-step

-------
OUTPUTS
-------
Plot: voltage against time
"""
import numpy as np
import matplotlib.pyplot as plt
def RLC(V0,L,C,R,T,dt):
    Q=V0*C
    I=0
    t=0
    w0 = 1/np.sqrt(L*C)
    V=[]
    I0 = []
    
    while t < T:
        n = V0/L*np.cos(w0*t) + Q/(L*C) - I*R/L
        I=I+n*dt
        Q=Q-I*dt
        t=t+dt
        V.append(Q/C)
        I0.append(I)
    
    fig, axs = plt.subplots(2)
    fig.suptitle('Oscilloscope Display')
    axs[0].plot(V)
    axs[1].plot(I0)
    axs.set_ylabel('Time Scale (T/dt)')
    axs[0].set(ylabel="Voltage [V]")
    axs[1].set(ylabel"Current [I]")
        
    
    
