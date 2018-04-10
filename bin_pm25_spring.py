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


pm25_LWT_info = np.empty([n_LWT])



c = pd.read_csv("/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/pm25_rural_data/pm25.csv", usecols=[0,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                         21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52])
print(c)
time.sleep(5)
        




data = []

start = 59 
stop = 151
counter = -1
print('outside loop', counter)
while counter <= 28: 
    for line in c:
        c = c.iloc[start:stop, :]
        print c
        #time.sleep(1)
        for row in c:
            data1 = c.loc[c['LWT'] == counter]
            data = data1.replace('No data', np.NaN)
            print('data=',data)
            data.append(data)
            #time.sleep(10)
            #pm25_LWT_info[counter] = data
            #data.to_csv("binned_pm25_spring_LWT_"+str(counter)+".csv",  na_rep="NaN", index=False, encoding='utf-8')
            time.sleep(2)
            counter = counter + 1 
        start = start + 365 
        stop = stop + 365
        print('inside loop', counter)
        print ('start',start,'stop',stop)
       
    print(data)
    data.to_csv("binned_pm25_spring_LWT_"+str(counter)+".csv",  na_rep="NaN", index=False, encoding='utf-8')

 
#    data = data.replace('No data', np.NaN)
#            
#            uc = [-1]
#            uc1 = [0]
#            uc2 = [20]
#            
#            
#            c = data.loc[(data['LWT']== uc) | (data['LWT']== uc1) | (data['LWT']== uc2)]
#            print('uc_data',c)
#            print type(c)
#            c.to_csv("binned_pm25_spring_uc"+".csv", na_rep="NaN", index=False, encoding='utf-8')
#            
#            ane =[1]
#            ne =[11]
#            cne =[21]
#            
#            c = data.loc[(data['LWT']== ane) | (data['LWT']== ne) | (data['LWT']== cne)]
#            print(c)
#            print type(c)
#            c.to_csv("binned_no2_kerbside_spring_ne"+".csv", na_rep="NaN", index=False, encoding='utf-8')
#            
#            ae=[2]
#            e=[12]
#            ce=[22]
#            
#            c = data.loc[(data['LWT']== ae) | (data['LWT']== e) | (data['LWT']== ce)]
#            print(c)
#            print type(c)
#            c.to_csv("binned_no2_kerbside_spring_e"+".csv", na_rep="NaN", index=False, encoding='utf-8')
#            
#            
#            ase=[3]
#            se=[13]
#            cse=[23]
#            
#            c = data.loc[(data['LWT']== ase) | (data['LWT']== se) | (data['LWT']== cse)]
#            print(c)
#            print type(c)
#            c.to_csv("binned_no2_kerbside_spring_se"+".csv", na_rep="NaN", index=False, encoding='utf-8')
#            
#            
#            a_s=[4]
#            s=[14]
#            cs=[24]
#            
#            c = data.loc[(data['LWT']== a_s) | (data['LWT']== s) | (data['LWT']== cs)]
#            print(c)
#            print type(c)
#            c.to_csv("binned_no2_kerbside_spring_s"+".csv", na_rep="NaN", index=False, encoding='utf-8')
#            
#            
#            asw=[5]
#            sw=[15]
#            csw=[25]
#            
#            c = data.loc[(data['LWT']== asw) | (data['LWT']== sw) | (data['LWT']== csw)]
#            print(c)
#            print type(c)
#            c.to_csv("binned_no2_kerbside_spring_sw"+".csv", na_rep="NaN", index=False, encoding='utf-8')
#            
#            
#            aw=[6]
#            w=[16]
#            cw=[26]
#            
#            c = data.loc[(data['LWT']== aw) | (data['LWT']== w) | (data['LWT']== cw)]
#            print(c)
#            print type(c)
#            c.to_csv("binned_no2_kerbside_spring_w"+".csv", na_rep="NaN", index=False, encoding='utf-8')
#            
#            
#            
#            anw=[7]
#            nw=[17]
#            cnw=[27]
#            
#            c = data.loc[(data['LWT']== anw) | (data['LWT']== nw) | (data['LWT']== cnw)]
#            print(c)
#            print type(c)
#            c.to_csv("binned_no2_kerbside_spring_nw"+".csv", na_rep="NaN", index=False, encoding='utf-8')
#            
#            
#            
#            an=[8]
#            n=[18]
#            cn=[28]
#            
#            c = data.loc[(data['LWT']== an) | (data['LWT']== n) | (data['LWT']== cn)]
#            print(c)
#            print type(c)
#            c.to_csv("binned_no2_kerbside_spring_n"+".csv", na_rep="NaN", index=False, encoding='utf-8')
#            



