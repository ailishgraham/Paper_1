#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 15:18:28 2018

@author: ee15amg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:13:05 2017

@author: ee15amg
"""
 
import pandas as pd
from pandas import DataFrame as frame
import numpy as np
import csv 
from operator import itemgetter, attrgetter
import glob, os
import time
import datetime


n_LWT = 30
n_days = 645
n_sites = 44

#pm_lwt = [n_LWT]
pm_LWT_info = np.empty([n_LWT])
#pm_LWT_info = np.empty([n_LWT,n_sites,n_days])

#a = pd.read_csv("LWT_2010_2016.csv")
#b = pd.read_csv("pm25_2010_2016.csv")
#b = b.dropna(axis=1)
#merged = a.merge(b, on='Date')
#merged.to_csv("lwt_pm25.csv", index=False)


df = pd.read_csv("no2_data_autumn.csv", usecols=[0,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                         21,22,23,24,25,26,27,28,29,30,31,32,33,
                                         34,35,36,37,38,39,40,41,42,43,44,45,46,
                                         47,48,49,50])
print 'before', df
c = df.replace('No data', np.NaN)
print 'after', c

counter = -1
print 'outside loop', counter
while counter <= 28: 
    for line in c:
        for row in c:
            data = c.loc[c['LWT'] == counter]
            print data
            data = data.replace('No data', 'np.NaN')
            print data
            #pm_LWT_info[counter] = data
            data.to_csv("binned__no2_autumn_LWT_"+str(counter)+".csv", na_rep="NaN", index=False, encoding='utf-8')
            time.sleep(3)
            counter = counter + 1 
        print 'inside loop', counter

    print data

