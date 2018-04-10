#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 16:20:57 2018

@author: ee15amg
"""


from mpl_toolkits.basemap import Basemap
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import colors
from mpl_toolkits.mplot3d import Axes3D
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
lwt_array = np.load('/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/scripts/lwt_pm25_data_checked.npy')
circ_array = np.load('/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/scripts/circ_pm25_data_checked.npy')
lwt_array_monthly = np.load('/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/scripts/lwt_pm25_data_checked_monthly.npy')
circ_array_monthly = np.load('/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/scripts/circ_pm25_data_checked_monthly.npy')
lwt_info = np.load('/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/scripts/data_yearly_lwt_classification.npy')

print(np.shape(lwt_array))
print(np.shape(circ_array))
print(np.shape(lwt_array_monthly))
print(np.shape(circ_array_monthly))
print(np.shape(lwt_info))

time.sleep(5)

# set array sizes to loop through

n_lwt = 8 
n_circ = 4
n_years = 7
n_months = 84
n_sites = 44
n_days = 365
n_days_month = 31

#Make arrays to add counts of occurences into
lwt_occurences = np.zeros([n_lwt,n_years,n_days])
circ_occurences = np.zeros([n_circ,n_years,n_days])
lwt_occurences_monthly = np.zeros([n_lwt,n_months,n_days_month])
circ_occurences_monthly = np.zeros([n_circ,n_months,n_days_month])

# Make temp arrays for average values
lwt_temp_all_sites = np.zeros([n_lwt,n_years,n_days])
lwt_temp_all_days = np.zeros([n_lwt,n_years])
lwt_temp_all_years = np.zeros([n_lwt])



# Add number of occurences of each lwt to arrays
for i_lwt in range(n_lwt):
    for i_year in range(n_years):
        for i_day in range(n_days):
            #print('lwt=',i_lwt, 'year =', i_year, 'day =', i_day)
            data = (lwt_array[i_lwt,i_year,:,i_day])
            #print('data =', data)
            occ = (float(len(data)) - (float(np.isnan(data).sum())))
            #print(occ)
            if occ > 0:
                add_count = 1
                #print('count =1')
                lwt_occurences[i_lwt,i_year,i_day] = add_count
    for i_month in range(n_months):
        for i_day in range(n_days_month):
            #print('lwt=',i_lwt, 'year =', i_year, 'day =', i_day)
            data_monthly = (lwt_array_monthly[i_lwt,i_month,:,i_day])
            #print('data =', data)
            occ = (float(len(data_monthly)) - (float(np.isnan(data_monthly).sum())))
            #print(occ)
            lwt_occurences_monthly[i_lwt,i_month,i_day] = occ
            #time.sleep(2)
            if occ > 0:
                add_count = 1
                #print('count =1')
                lwt_occurences_monthly[i_lwt,i_month,i_day] = add_count
                           
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
                #time.sleep(2)~
    for i_month in range(n_months):
        for i_day in range(n_days_month):
            #print('circ=',i_circ, 'month =', i_month, 'day =', i_day)
            data_monthly = (circ_array_monthly[i_circ,i_month,:,i_day])
            #print('data =', data)
            occ = (float(len(data_monthly)) - (float(np.isnan(data_monthly).sum())))
            #print(occ)           
            if occ > 0:
                add_count = 1
                #print('count =1')
                circ_occurences_monthly[i_circ,i_month,i_day] = add_count
                
print(np.shape(circ_occurences))

for i_lwt in range(n_lwt):
    for i_year in range(n_years):
        for i_day in range(n_days):
            #print('lwt = ',i_lwt,'year = ',i_year, 'day = ', i_day)
            temp_data_all_sites = lwt_array[i_lwt,i_year,:,i_day]
            #print('values = ' , np.count_nonzero(~np.isnan(temp_data_all_sites)))
            av_td_all_sites = np.nanmean(temp_data_all_sites)
            #print('av =', av_td_all_sites)
            lwt_temp_all_sites[i_lwt,i_year,i_day]=av_td_all_sites
            #time.sleep(2)
print('conc = ', np.shape(lwt_temp_all_sites))
print('occ = ', np.shape(lwt_occurences))
print('lwt_info = ', np.shape(lwt_info))
time.sleep(10)

n_bins = 11
bins = np.arange(0,100,10)
binned_data = np.zeros([n_lwt,n_years,n_days,n_bins])
binned_data[:,:,:,:]=np.nan
lwt_occurences_binned=np.zeros([n_lwt,n_years,n_days,n_bins])
lwt_occurences_binned[:,:,:,:]=np.nan
#print('binned data', binned_data)

for i_lwt in range(n_lwt):
    for i_year in range(n_years):
        for i_day in range(n_days):
            x = lwt_temp_all_sites[i_lwt,i_year,i_day]
            lwt_data = lwt_occurences[i_lwt,i_year,i_day]
            inds = float(np.digitize(x, bins))
            #inds = float(inds)
            #print('lwt',i_lwt,'year',i_year,'day',i_day)
            print('inds = ', inds)
            #print('inds-1',inds-1)
            #time.sleep(2)
            #for i in range(x.size):
            if inds==10.0:
                #print('flag',np.nan)
                binned_data[i_lwt,i_year,i_day,inds]=np.nan
            else:
                print('x =' ,x)
                print('lwt_data = ', lwt_data)
                binned_data[i_lwt,i_year,i_day,inds-1]=x
                lwt_occurences_binned[i_lwt,i_year,i_day,inds-1]=lwt_data
print(lwt_occurences_binned)
binned_data = np.ma.masked_invalid(binned_data)  
lwt_occurences_binned = np.ma.masked_invalid(lwt_occurences_binned)


y_pos = []
x_pos = []
z_pos= []
dx = []
dy = []
dz = []
lwt_vals = [0,1,2,3,4,5,6,7,8]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')   

for i_lwt in range(n_lwt):
#for i_year in range(n_years): ## use year 5 for now
    for i_bin in range(n_bins-1):    
        y_data = binned_data[i_lwt,:,:,i_bin]
        y_pos.append(np.nanmean(y_data))
        #print('y_value',y_pos)
        x_pos.append(i_lwt)
        z_pos.append(0)
        
        dx.append(1)
        dy.append(10)
        dz_data = ((np.size(lwt_occurences_binned[i_lwt,:,:,i_bin]))-(np.ma.count_masked(lwt_occurences_binned[i_lwt,:,:,i_bin])))
        dz.append(dz_data)
        #print('dz = ', dz)
        
        print('ypos',y_pos,'xpos',x_pos,'zpos',z_pos,
              'dx',dx,'dy',dy,'dz',dz)
time.sleep(2)
ax.bar3d(x_pos,y_pos,z_pos,dx,dy,dz, color = 'r')
labels = [ 'N','NE','E','SE','S','SW','W','NW' ]
ax.set_xlabel('Lamb Weather Type')
ax.set_ylabel('PM$_{2.5}$ Concentration')
ax.set_zlabel('Occurence')
plt.xticks(lwt_vals, labels)
plt.title('The occurence and associated conentration of \n Lamb Weather Types 2010-2016')
plt.show()

print('ypos', y_pos)
print('x_pos', x_pos)
print('dz', dz)
