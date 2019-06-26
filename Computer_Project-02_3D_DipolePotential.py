# -*- coding: utf-8 -*-
"""
Purpose: To plot the field of an electrostatic dipole in three dimensions
Author: Kurt Burdick
date modified: 9/26/18
"""

from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

#define constants
k = 8.99e9
q = 1.602e-19

#make data for the grids 3D Plot 
X = np.arange(-2, 2, 0.25)
xlen = len(X)
Y = np.arange(-2, 2, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
R_p = np.sqrt((X**2) + ((Y+0.005)**2))
R_e = np.sqrt((X**2) + ((Y-0.005)**2))

#functions for the Electric Potential of positive and negative charges
Z = ( (k*q)/((R_p) ))
 
Z2 = ( (k*-q)/((R_e) )) 

Z_t = Z + Z2

#plot the graph, make labels, and set axes limit
ax = plt.axes(projection='3d')
contour1 = ax.contour3D(X, Y, Z_t, 200, cmap='coolwarm')
ax.set_xlabel('X-Distance')
ax.set_ylabel('Y-Distance')
ax.set_zlabel('Potential')
ax.set_zlim(-8e-10, 8e-10) #use of proper scale 
plt.show()