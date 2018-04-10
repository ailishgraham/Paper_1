#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:24:43 2018

@author: ee15amg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:16:43 2018

@author: ee15amg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:08:54 2018

@author: ee15amg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 10:44:10 2018

@author: ee15amg
"""

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

filestem = '/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/bin_no2_data/binned_no2_winter_'
filestem1 = '/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/bin_no2_data/binned_no2_kerbside_winter_'

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
    df = df.replace('No data', np.NaN)
    df = df[df.columns[2:44]]
    df = df.convert_objects(convert_numeric=True)
    print df

    n_row = np.shape(df)[0]
    n_col = np.shape(df)[1]
    d = df.values
    print('min',np.min(d), 'max',np.max(d))

   
    n_rows = np.shape(d)[0]
    #print 'n_rows', n_rows
    n_cols = np.shape(d)[1]
    #print 'n_cols', n_cols
    n_datapoints = n_cols*n_rows
    #print 'n_datapoints', n_datapoints
    
    d_flattened = np.ndarray.flatten(d)
    print 'flat', d_flattened

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


statistics1 = np.zeros([n_stats,n_lwt])


for lwt in np.arange(len(lamb_weather_type)):
    df1 = pd.read_csv(file_list1[lwt], index_col=None)
    print df1

    df = df1.replace('No data', np.NaN)
    df = df[df.columns[2:44]]
    df = df.convert_objects(convert_numeric=True)
    print df

    n_row = np.shape(df)[0]
    n_col = np.shape(df)[1]

    d1 = df.values
    
    print('min',np.min(d1), 'max',np.max(d1))

   
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


anomaly_no2 = np.zeros([n_stats,n_lwt])

for i_stat in range(n_stats):
    for i_lwt in np.arange(len(lamb_weather_type)):
        temp_stat = (statistics_1[i_stat,i_lwt] - statistics[i_stat,i_lwt])
        anomaly_no2[i_stat,i_lwt] = temp_stat
        #print i_stat, i_lwt, temp_stat 
        #time.sleep(1)
print np.size(anomaly_no2), anomaly_no2[:,:]



offset = 0.3
lwt_val = [0,1,2,3,4,5,6,7,8]
f, ax = plt.subplots()
for i in range(n_lwt):  
    
    ax.plot([lwt_val[i]-offset,lwt_val[i]+offset],[anomaly_no2[0,i],anomaly_no2[0,i]], 'r-') 
    ax.plot([lwt_val[i]-offset,lwt_val[i]+offset],[anomaly_no2[1,i],anomaly_no2[1,i]], 'b-')
    ax.plot([lwt_val[i]-offset,lwt_val[i]+offset],[anomaly_no2[2,i],anomaly_no2[2,i]], 'b-')
    ax.plot([lwt_val[i]-offset,lwt_val[i]+offset],[anomaly_no2[4,i],anomaly_no2[4,i]], 'b-')
    ax.plot([lwt_val[i]-offset,lwt_val[i]+offset],[anomaly_no2[3,i],anomaly_no2[3,i]], 'b-')
    ax.plot([lwt_val[i]-offset,lwt_val[i]-offset],[anomaly_no2[1,i],anomaly_no2[2,i]], 'b-')
    ax.plot([lwt_val[i]+offset,lwt_val[i]+offset],[anomaly_no2[1,i],anomaly_no2[2,i]], 'b-')
    ax.plot([lwt_val[i],lwt_val[i]],[anomaly_no2[4,i],anomaly_no2[1,i]], 'b-')
    ax.plot([lwt_val[i],lwt_val[i]],[anomaly_no2[2,i],anomaly_no2[3,i]], 'b-')
    
plt.show