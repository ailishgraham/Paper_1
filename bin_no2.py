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
n_days = 2557
n_sites = 44


no2_LWT_info = np.empty([n_LWT])



c = pd.read_csv("/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/raw_no2_data/no2_kerbside_only.csv", usecols=[0,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                         21,22,23,24,25,26,27,28,29])
print(c)
time.sleep(10)
        







counter = -1
print('outside loop', counter)
while counter <= 28: 
    for line in c:
        for row in c:
            data1 = c.loc[c['LWT'] == counter]
            data = data1.replace('No data', np.NaN)
            print('data=',data)
            #time.sleep(10)
            #no2_LWT_info[counter] = data
            data.to_csv("binned_kerbside_no2_LWT_"+str(counter)+".csv",  na_rep="NaN", index=False, encoding='utf-8')
            time.sleep(10)
            counter = counter + 1 
        print('inside loop', counter)

    print(data)

 



