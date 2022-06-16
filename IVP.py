# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 12:51:40 2022

@author: Farzad
"""
# %reset -f

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Defining the function

def modelLower(y,t):
    y1=y[0]
    y2=y[1]
    p1=0.3
    p2=1.9255
    p3=0.1451
    dy1dt=-(p1+p3)*y1+p2*y2
    dy2dt=p3*y1-p2*y2
    return [dy1dt,dy2dt]

    
def modelUpper(y,t):
    y1=y[0]
    y2=y[1]
    p1=0.2
    p2=1.9255
    p3=0.1451
    dy1dt=-(p1+p3)*y1+p2*y2
    dy2dt=p3*y1-p2*y2
    return [dy1dt,dy2dt]

# Initial Condition

y0=[1,0]

# Time points

t=np.linspace(0,16,50, endpoint=True)

# Solve Verified ODE for Lower

yL= odeint(modelLower,y0,t)
yU= odeint(modelUpper,y0,t)

y1L=yL[:,0]
y2L=yL[:,1]

y1U=yU[:,0]
y2U=yU[:,1]


#Plot Results
plt.figure()
plt.plot(t,y1L,'r-',t,y2L,'r-',t,y1U,'b--',t,y2U,'b--')
plt.legend()
plt.ylabel('y1L , y2L, y1U, y2U')
plt.xlabel('Time')
plt.title(' Two Comparment Model Plotting In Python ')
