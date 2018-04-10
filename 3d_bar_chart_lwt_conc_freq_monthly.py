#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 11:28:37 2018

@author: ee15amg
"""

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
#Dimensions of array (n_circ,n_months,n_sites,n_days)
lwt_array_monthly = np.load('/nfs/a216/ee15amg/AURN_data/scripts/lwt_pm25_data_checked_monthly.npy')
circ_array = np.load('/nfs/a216/ee15amg/AURN_data/scripts/circ_pm25_data_checked_monthly.npy')
lwt_class_array = np.load('/nfs/a216/ee15amg/AURN_data/scripts/data_yearly_lwt_classification.npy')

print(np.shape(lwt_array_monthly))
print(np.shape(circ_array))
print(np.shape(lwt_class_array))
time.sleep(5)

n_lwt = 8 
n_circ = 4
n_months = 84
n_sites = 44
n_days = 31

#Make arrays to add counts of occurences into
lwt_occurences = np.zeros([n_lwt,n_months,n_days])
circ_occurences = np.zeros([n_circ,n_months,n_days])

# Add number of occurences of each lwt to arrays
for i_lwt in range(n_lwt):
    for i_month in range(n_months):
        for i_day in range(n_days):
            #print('lwt=',i_lwt, 'year =', i_month, 'day =', i_day)
            data = (lwt_array_monthly[i_lwt,i_month,:,i_day])
            #print('data =', data)
            occ = (float(len(data)) - (float(np.isnan(data).sum())))
            #print(occ)
            lwt_occurences[i_lwt,i_month,i_day] = occ
            #time.sleep(2)
            if occ > 0:
                add_count = 1
                #print('count =1')
                lwt_occurences[i_lwt,i_month,i_day] = add_count
                
# Add number of occurences of each circ type to arrays
for i_circ in range(n_circ):
    for i_month in range(n_months):
        for i_day in range(n_days):
            #print('circ=',i_circ, 'year =', i_month, 'day =', i_day)
            data = (circ_array[i_circ,i_month,:,i_day])
            #print('data =', data)
            occ = ((float(len(data)) - (float(np.isnan(data).sum()))))
            #print(occ)
            if occ > 0:
                add_count = 1
                #print('count =1')
                circ_occurences[i_circ,i_month,i_day] = add_count
                #print(circ_occurences[i_circ,i_month,i_day])
                #time.sleep(2)

print('lwtshape', np.shape(lwt_array_monthly), 'circshape',np.shape(circ_array),
      'countlwt',np.shape(lwt_occurences), 'countcirc', np.shape(circ_occurences))


n_bins = 9 
binned_data_array = np.zeros([n_lwt,n_months,n_sites,n_days,n_bins])

bins = np.linspace(0,70,8)
print('bins', bins)
time.sleep(5)
for i_lwt in range(n_lwt):
    for i_month in range(n_months):
        for i_site in range(n_sites):
            for i_day in range(n_days):
                data_to_bin = (lwt_array_monthly[i_lwt, i_month, i_site, i_day])
                #print(' D2B',(data_to_bin))
                #print('non-nan', data_to_bin[~np.isnan(data_to_bin)])
                inds = np.digitize(data_to_bin, bins)
                #print('inds', inds)
                #print( i_lwt, i_month, i_site, i_day, inds)
                add_count = 1
                binned_data_array[i_lwt,i_month,i_site,i_day,inds] = add_count

for i_lwt in range(n_lwt):
    print('lwt = ', i_lwt)
    for i_bin in range(n_bins):
        print( 'bin', i_bin)
        print(np.count_nonzero(binned_data_array[i_lwt,:,:,:,i_bin]))    
        




#x = np.arange(n_months)
#counter = 0 
#while counter < 8:
#    for i_month in range(n_months):
#        y = np.ndarray.flatten(lwt_occurences[counter,i_month,:])
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