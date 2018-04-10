#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:16:04 2018

@author: ee15amg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 11:03:08 2018

@author: ee15amg
"""

#!/bin/env python

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import glob, os
import re
import time

filestem = '/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/bin_no2_data/binned_no2_spring_LWT_'
filestem1 = '/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/bin_no2_data/binned_no2_kerbside_spring_'
lamb_weather_type = ['n','e','s','w','ne','nw','se','sw','uc']

file_list= []
for count in lamb_weather_type:
   fn = filestem+str(count)+'.csv'
   file_list.append( fn )
print(file_list)
# Debug help
###for f in file_list:
###   print f

n_stats = 5
n_lwt = len(lamb_weather_type)
statistics = np.zeros([n_stats,n_lwt])
statistics_1 = np.zeros([n_stats,n_lwt])



for lwt in np.arange(len(lamb_weather_type)):
    df = pd.read_csv(file_list[lwt], index_col=None)
    #print df
    #time.sleep(100)
    #print(type(data))
    df = df.replace('No data', np.NaN)
    df = df[df.columns[2:44]]
    df = df.convert_objects(convert_numeric=True)
    print df

    n_row = np.shape(df)[0]
    n_col = np.shape(df)[1]

    #d = df.as_matrix(columns=[df.columns[2:43]])
    d = df.values
    
    
    #print('data_matrix', d)
    print('min',np.min(d), 'max',np.max(d))
    #print(np.shape(d))

    #time.sleep(100)
   
    n_rows = np.shape(d)[0]
    #print 'n_rows', n_rows
    n_cols = np.shape(d)[1]
    #print 'n_cols', n_cols
    n_datapoints = n_cols*n_rows
    #print 'n_datapoints', n_datapoints
    
    d_flattened = np.ndarray.flatten(d)
    #d_flattened = np.reshape(d, n_datapoints)
    print 'flat', d_flattened
    #print("bef ",np.shape(d_flattened)) 
    #print(d_flattened, d_flattened[1])#
    
    #time.sleep(100)
    centile50 = np.nanpercentile(d_flattened, 50)
    statistics[0,lwt]= centile50
    centile25 = np.nanpercentile(d_flattened, 25)
    statistics[1,lwt]= centile25
    centile75 = np.nanpercentile(d_flattened, 75)
    statistics[2,lwt]= centile75
    centile90 = np.nanpercentile(d_flattened, 90)
    statistics[3,lwt]= centile90
    centile10 = np.nanpercentile(d_flattened, 10)
    statistics[4,lwt]= centile10


    
#    print("centile10 = ",centile10)
#    print("centile25 = ",centile25)
#    print("centile50 = ",centile50)
#    print("centile75 = ",centile75)
#    print("centile90 = ",centile90)
#    print(statistics[:,:]), 'stats'
#    print(statistics.shape)
    
    
    
    
file_list1= []
for count in lamb_weather_type:
   fn1 = filestem1+str(count)+'.csv'
   file_list1.append( fn1 )
print(file_list1)

# Debug help
###for f in file_list:
###   print f

n_stats1 = 5
n_lwt1 = len(lamb_weather_type)
statistics1 = np.zeros([n_stats,n_lwt])


for lwt in np.arange(len(lamb_weather_type)):
    df1 = pd.read_csv(file_list1[lwt], index_col=None)
    print df1
    #print df
    #time.sleep(100)
    #print(type(data))
    df = df1.replace('No data', np.NaN)
    df = df[df.columns[2:44]]
    df = df.convert_objects(convert_numeric=True)
    print df

    n_row = np.shape(df)[0]
    n_col = np.shape(df)[1]

    #d = df.as_matrix(columns=[df.columns[2:43]])
    d1 = df.values
    
    #print('data_matrix', d)
    print('min',np.min(d1), 'max',np.max(d1))
    #print(np.shape(d))

    #time.sleep(100)
   
    n_rows = np.shape(d1)[0]
    print 'n_rows', n_rows
    n_cols = np.shape(d1)[1]
    print 'n_cols', n_cols
    n_datapoints = n_cols*n_rows
    print 'n_datapoints', n_datapoints
    
    d1_flattened = np.ndarray.flatten(d1)
    d1_flattened = np.reshape(d1, n_datapoints)
    
    print 'flat', d_flattened
    print 'flat1', d1_flattened
    #print("bef ",np.shape(d_flattened)) 
    #print(d_flattened, d_flattened[1])#
    
    #time.sleep(100)
    centile50_1 = np.nanpercentile(d1_flattened, 50)
    statistics_1[0,lwt]= centile50_1 
    centile25_1 = np.nanpercentile(d1_flattened, 25)
    statistics_1[1,lwt]= centile25_1 
    centile75_1 = np.nanpercentile(d1_flattened, 75)
    statistics_1[2,lwt]= centile75_1 
    centile90_1 = np.nanpercentile(d1_flattened, 90)
    statistics_1[3,lwt]= centile90_1 
    centile10_1 = np.nanpercentile(d1_flattened, 10)
    statistics_1[4,lwt]= centile10_1 

    


offset = 0.3
lwt_val0 = [0,1,2,3,4,5,6,7,8]
lwt_val1 = [0,1,2,3,4,5,6,7,8]
#lwt_val = [0,1,2,3,4,5,6,7,8]
#f, (ax1, ax0) = plt.subplots(1, 2)
f, (ax0, ax1) = plt.subplots(2, sharex=True, sharey=True)
#fig=plt.figure(figsize=(15,5.5))
#ax0=plt.subplot2grid((1,2),(0,0))
#ax1=plt.subplot2grid((1,2),(0,1))

#f, ax = plt.subplots()
for i in range(n_lwt):   
#
#    ax.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[0,i],statistics[0,i]], 'r-') 
#    ax.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[1,i],statistics[1,i]], 'b-')
#    ax.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[2,i],statistics[2,i]], 'b-')
#    ax.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[4,i],statistics[4,i]], 'b-')
#    ax.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[3,i],statistics[3,i]], 'b-')
#    ax.plot([lwt_val[i]-offset,lwt_val[i]-offset],[statistics[1,i],statistics[2,i]], 'b-')
#    ax.plot([lwt_val[i]+offset,lwt_val[i]+offset],[statistics[1,i],statistics[2,i]], 'b-')
#    ax.plot([lwt_val[i],lwt_val[i]],[statistics[4,i],statistics[1,i]], 'b-')
#    ax.plot([lwt_val[i],lwt_val[i]],[statistics[2,i],statistics[3,i]], 'b-')

    
    ax0.plot([lwt_val0[i]-offset,lwt_val0[i]+offset],[statistics[0,i],statistics[0,i]], 'r-') 
    ax0.plot([lwt_val0[i]-offset,lwt_val0[i]+offset],[statistics[1,i],statistics[1,i]], 'b-')
    ax0.plot([lwt_val0[i]-offset,lwt_val0[i]+offset],[statistics[2,i],statistics[2,i]], 'b-')
    ax0.plot([lwt_val0[i]-offset,lwt_val0[i]+offset],[statistics[4,i],statistics[4,i]], 'b-')
    ax0.plot([lwt_val0[i]-offset,lwt_val0[i]+offset],[statistics[3,i],statistics[3,i]], 'b-')
    ax0.plot([lwt_val0[i]-offset,lwt_val0[i]-offset],[statistics[1,i],statistics[2,i]], 'b-')
    ax0.plot([lwt_val0[i]+offset,lwt_val0[i]+offset],[statistics[1,i],statistics[2,i]], 'b-')
    ax0.plot([lwt_val0[i],lwt_val0[i]],[statistics[4,i],statistics[1,i]], 'b-')
    ax0.plot([lwt_val0[i],lwt_val0[i]],[statistics[2,i],statistics[3,i]], 'b-')
#    
    
    #ax1 = f.add_subplot(2,1,1, axisbg='grey')
    ax1.plot([lwt_val1[i]-offset,lwt_val1[i]+offset],[statistics_1[0,i],statistics_1[0,i]], 'r-') 
    ax1.plot([lwt_val1[i]-offset,lwt_val1[i]+offset],[statistics_1[1,i],statistics_1[1,i]], 'b-')
    ax1.plot([lwt_val1[i]-offset,lwt_val1[i]+offset],[statistics_1[2,i],statistics_1[2,i]], 'b-')
    ax1.plot([lwt_val1[i]-offset,lwt_val1[i]+offset],[statistics_1[4,i],statistics_1[4,i]], 'b-')
    ax1.plot([lwt_val1[i]-offset,lwt_val1[i]+offset],[statistics_1[3,i],statistics_1[3,i]], 'b-')
    ax1.plot([lwt_val1[i]-offset,lwt_val1[i]-offset],[statistics_1[1,i],statistics_1[2,i]], 'b-')
    ax1.plot([lwt_val1[i]+offset,lwt_val1[i]+offset],[statistics_1[1,i],statistics_1[2,i]], 'b-')
    ax1.plot([lwt_val1[i],lwt_val1[i]],[statistics_1[4,i],statistics_1[1,i]], 'b-')
    ax1.plot([lwt_val1[i],lwt_val1[i]],[statistics_1[2,i],statistics_1[3,i]], 'b-')

labels0 = [ 'n','e','s','w','ne','nw','se','sw','uc' ]
labels1 = [ 'n','e','s','w','ne','nw','se','sw','uc' ]
ax0.set_xlim((-1,9))
ax0.set_ylim((0,100))
ax1.set_xlim((-1,9))
ax1.set_ylim((0,100))
#ax0.set_xticks(lwt_val0, labels0)
#ax1.set_xticks(lwt_val1,labels1)
plt.xticks(lwt_val0, labels0)
ax0.set_title('Background vs Kerbside Spring NO$_{2}$ Concentrations & \n combined  LWT 2010-2016')
ax0.set_ylabel('NO$_{2}$ Concentration')
#ax1.set_title('Kerbside Spring NO$_{2}$ \n Concentrations & \n combined LWT 2010-2016')
ax1.set_ylabel('NO$_{2}$ Concentration')
#ax0.set_xlabel('Lamb Weather Type')
ax1.set_xlabel('Lamb Weather Type')
f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('merged_lwt_no2_kerbside_background_spring.png')
plt.show()
