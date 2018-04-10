#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:29:29 2018

@author: ee15amg
"""

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame as frame
import numpy as np
import csv 
from operator import itemgetter, attrgetter
import glob, os
import time
import datetime
from datetime import datetime
import math
from scipy import stats


#Read in lwt array for annual checked data 
#Dimensions of array (n_circ,n_years,n_sites,n_days)
lwt_array = np.load('lwt_pm25_data_checked.npy')
circ_array = np.load('circ_pm25_data_checked.npy')
lwt_class_array = np.load('data_yearly_lwt_classification.npy')

print(np.shape(lwt_array))
print(np.shape(circ_array))
print(np.shape(lwt_class_array))
time.sleep(5)

n_lwt = 8 
n_circ = 4
n_years = 7
n_sites = 44
n_days = 365

#Make arrays to add counts of occurences into
lwt_occurences = np.zeros([n_lwt,n_years,n_days])
circ_occurences = np.zeros([n_circ,n_years,n_days])

# Add number of occurences of each lwt to arrays
for i_lwt in range(n_lwt):
    for i_year in range(n_years):
        for i_day in range(n_days):
            #print('lwt=',i_lwt, 'year =', i_year, 'day =', i_day)
            data = (lwt_array[i_lwt,i_year,:,i_day])
            #print('data =', data)
            occ = (float(len(data)) - (float(np.isnan(data).sum())))
            #print(occ)
            lwt_occurences[i_lwt,i_year,i_day] = occ
            #time.sleep(2)
            if occ > 0:
                add_count = 1
                #print('count =1')
                lwt_occurences[i_lwt,i_year,i_day] = add_count
                
# Add number of occurences of each circ type to arrays
for i_circ in range(n_circ):
    for i_year in range(n_years):
        for i_day in range(n_days):
            #print('circ=',i_circ, 'year =', i_year, 'day =', i_day)
            data = (circ_array[i_circ,i_year,:,i_day])
            #print('data =', data)
            occ = ((float(len(data)) - (float(np.isnan(data).sum()))))
            #print(occ)
            if occ > 0:
                add_count = 1
                #print('count =1')
                circ_occurences[i_circ,i_year,i_day] = add_count
                #print(circ_occurences[i_circ,i_year,i_day])
                #time.sleep(2)

print('lwtshape', np.shape(lwt_array), 'circshape',np.shape(circ_array),
      'countlwt',np.shape(lwt_occurences), 'countcirc', np.shape(circ_occurences))


# setup the figure and axes
fig = plt.figure(figsize=(8, 3))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel("x")
ax.set_ylabel("y") 
ax.set_zlabel("z")
ax.set_xlim3d(0,10)
ax.set_ylim3d(0,10) 

xpos = [2,5,8,2,5,8,2,5,8]
ypos = [1,1,1,5,5,5,9,9,9]
zpos = np.zeros(9)

print('xpos',xpos)
time.sleep(2)
print('ypos',ypos)
time.sleep(2)
print('zpos',zpos)
time.sleep(2)

dx = np.ones(9)
dy = np.ones(9)
dz = [np.random.random(9) for i in range(4)]  # the heights of the 4 bar sets

print('dx',dx)
time.sleep(2)
print('dy',dy)
time.sleep(2)
print('dz',dz)
time.sleep(2)

_zpos = zpos   # the starting zpos for each bar
colors = ['r', 'b', 'g', 'y']
for i in range(4):
    ax.bar3d(xpos, ypos, _zpos, dx, dy, dz[i], color=colors[i])
    _zpos += dz[i]    # add the height of each bar to know where to start the next

plt.gca().invert_xaxis()
plt.show()






#%%
x = [0] * 2920
y = np.ndarray.flatten(lwt_occurences[:,0,:])
print len(y)

#_xx, _yy = np.meshgrid(_x, _y)
#x, y = _xx.ravel(), _yy.ravel()

top = counter
bottom = np.zeros_like(top)
print('x',x)
time.sleep(5)
print('y',y)
time.sleep(5)
print('top',top)
time.sleep(5)
print('lens', len(x),len(y),len(top))

width = depth = 1

ax1.bar3d(x, y, bottom, width, depth, top)
ax1.set_title('Shaded')
plt.show()


#x = np.arange(n_years)
#counter = 0 
#while counter < 8:
#    for i_year in range(n_years):
#        y = np.ndarray.flatten(lwt_occurences[counter,i_year,:])
##_xx, _yy = np.meshgrid(_x, _y)
##x, y = _xx.ravel(), _yy.ravel()
#    
#    top = counter
#    bottom = np.zeros_like(top)
#    print('x',x)
#    time.sleep(5)
#    print('y',y)
#    time.sleep(5)
#    print('top',top)
#    time.sleep(5)
#    print('lens', len(x),len(y),len(top))
#    
#    width = depth = 1
#    
#    ax1.bar3d(x, y, bottom, width, depth, top)
#    ax1.set_title('Shaded')
#    plt.show()