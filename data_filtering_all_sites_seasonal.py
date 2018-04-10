#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:58:09 2018

@author: ee15amg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:22:01 2018

@author: ee15amg
"""


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

## Read in data from pm25.csv 

df = pd.read_csv("/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/pm25_rural_data/pm25.csv",parse_dates=[0],usecols=[0,9,10,11,12,13,14,15,16,17,18,19,20,
                                         21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52])
df_lwt = pd.read_csv("/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/pm25_rural_data/pm25.csv",usecols=[0,8])
#print df.head()
#print df_lwt.head()


## Replace Date String with Datetime

df = df.replace('No data', np.NaN)
df['Date'] = pd.to_datetime(df['Date'])
#print 'datetype', type(date)
#print df['Date'], type(df['Date']),np.shape(df['Date']), len(df['Date'])
df = df.set_index(['Date'])

## Set Date as index in LWT dataframe 
df_lwt['Date'] = pd.to_datetime(df_lwt['Date'])
df_lwt = df_lwt.set_index(['Date'])


## Dates to loop over ##

data_month = ['jan2010', 'feb2010', 'mar2010', 'apr2010', 'may2010', 'jun2010', 
              'jul2010', 'aug2010', 'sept2010', 'oct2010', 'nov2010', 'dec2010',
              'jan2011', 'feb2011', 'mar2011', 'apr2011', 'may2011', 'jun2011', 
              'jul2011', 'aug2011', 'sept2011', 'oct2011', 'nov2011', 'dec2011',
              'jan2012', 'feb2012', 'mar2012', 'apr2012', 'may2012', 'jun2012', 
              'jul2012', 'aug2012', 'sept2012', 'oct2012', 'nov2012', 'dec2012',
              'jan2013', 'feb2013', 'mar2013', 'apr2013', 'may2013', 'jun2013', 
              'jul2013', 'aug2013', 'sept2013', 'oct2013', 'nov2013', 'dec2013',
              'jan2014', 'feb2014', 'mar2014', 'apr2014', 'may2014', 'jun2014', 
              'jul2014', 'aug2014', 'sept2014', 'oct2014', 'nov2014', 'dec2014',
              'jan2015', 'feb2015', 'mar2015', 'apr2015', 'may2015', 'jun2015', 
              'jul2015', 'aug2015', 'sept2015', 'oct2015', 'nov2015', 'dec2015',
              'jan2016', 'feb2016', 'mar2016', 'apr2016', 'may2016', 'jun2016', 
              'jul2016', 'aug2016', 'sept2016', 'oct2016', 'nov2016', 'dec2016']

month_start_look_up = ['2010-01-01', '2010-02-01', '2010-03-01', '2010-04-01',
                       '2010-05-01', '2010-06-01', '2010-07-01', '2010-08-01',
                       '2010-09-01', '2010-10-01', '2010-11-01', '2010-12-01',
                       '2011-01-01', '2011-02-01', '2011-03-01', '2011-04-01',
                       '2011-05-01', '2011-06-01', '2011-07-01', '2011-08-01',
                       '2011-09-01', '2011-10-01', '2011-11-01', '2011-12-01',
                       '2012-01-01', '2012-02-01', '2012-03-01', '2012-04-01',
                       '2012-05-01', '2012-06-01', '2012-07-01', '2012-08-01',
                       '2012-09-01', '2012-10-01', '2012-11-01', '2012-12-01',
                       '2013-01-01', '2013-02-01', '2013-03-01', '2013-04-01',
                       '2013-05-01', '2013-06-01', '2013-07-01', '2013-08-01',
                       '2013-09-01', '2013-10-01', '2013-11-01', '2013-12-01',
                       '2014-01-01', '2014-02-01', '2014-03-01', '2014-04-01',
                       '2014-05-01', '2014-06-01', '2014-07-01', '2014-08-01',
                       '2014-09-01', '2014-10-01', '2014-11-01', '2014-12-01',
                       '2015-01-01', '2015-02-01', '2015-03-01', '2015-04-01',
                       '2015-05-01', '2015-06-01', '2015-07-01', '2015-08-01',
                       '2015-09-01', '2015-10-01', '2015-11-01', '2015-12-01',
                       '2016-01-01', '2016-02-01', '2016-03-01', '2016-04-01',
                       '2016-05-01', '2016-06-01', '2016-07-01', '2016-08-01',
                       '2016-09-01', '2016-10-01', '2016-11-01', '2016-12-01']

month_end_look_up = ['2010-01-31', '2010-02-28', '2010-03-31', '2010-04-30',
                     '2010-05-31', '2010-06-30', '2010-07-31', '2010-08-31',
                     '2010-09-30', '2010-10-31', '2010-11-30', '2010-12-31',
                     '2011-01-31', '2011-02-28', '2011-03-31', '2011-04-30',
                     '2011-05-31', '2011-06-30', '2011-07-31', '2011-08-31',
                     '2011-09-30', '2011-10-31', '2011-11-30', '2011-12-31',
                     '2012-01-31', '2012-02-29', '2012-03-31', '2012-04-30',
                     '2012-05-31', '2012-06-30', '2012-07-31', '2012-08-31',
                     '2012-09-30', '2012-10-31', '2012-11-30', '2012-12-31',
                     '2013-01-31', '2013-02-28', '2013-03-31', '2013-04-30',
                     '2013-05-31', '2013-06-30', '2013-07-31', '2013-08-31',
                     '2013-09-30', '2013-10-31', '2013-11-30', '2013-12-31',
                     '2014-01-31', '2014-02-28', '2014-03-31', '2014-04-30',
                     '2014-05-31', '2014-06-30', '2014-07-31', '2014-08-31',
                     '2014-09-30', '2014-10-31', '2014-11-30', '2014-12-31',
                     '2015-01-31', '2015-02-28', '2015-03-31', '2015-04-30',
                     '2015-05-31', '2015-06-30', '2015-07-31', '2015-08-31',
                     '2015-09-30', '2015-10-31', '2015-11-30', '2015-12-31',
                     '2016-01-31', '2016-02-29', '2016-03-31', '2016-04-30',
                     '2016-05-31', '2016-06-30', '2016-07-31', '2016-08-31',
                     '2016-09-30', '2016-10-31', '2016-11-30', '2016-12-31']

month_length = [31,28,31,30,31,30,31,31,30,31,30,31,
                31,28,31,30,31,30,31,31,30,31,30,31,
                31,28,31,30,31,30,31,31,30,31,30,31,
                31,28,31,30,31,30,31,31,30,31,30,31,
                31,28,31,30,31,30,31,31,30,31,30,31,
                31,28,31,30,31,30,31,31,30,31,30,31,
                31,28,31,30,31,30,31,31,30,31,30,31]

data_month_lwt = ['jan2010', 'feb2010', 'mar2010', 'apr2010', 'may2010', 'jun2010', 
              'jul2010', 'aug2010', 'sept2010', 'oct2010', 'nov2010', 'dec2010',
              'jan2011', 'feb2011', 'mar2011', 'apr2011', 'may2011', 'jun2011', 
              'jul2011', 'aug2011', 'sept2011', 'oct2011', 'nov2011', 'dec2011',
              'jan2012', 'feb2012', 'mar2012', 'apr2012', 'may2012', 'jun2012', 
              'jul2012', 'aug2012', 'sept2012', 'oct2012', 'nov2012', 'dec2012',
              'jan2013', 'feb2013', 'mar2013', 'apr2013', 'may2013', 'jun2013', 
              'jul2013', 'aug2013', 'sept2013', 'oct2013', 'nov2013', 'dec2013',
              'jan2014', 'feb2014', 'mar2014', 'apr2014', 'may2014', 'jun2014', 
              'jul2014', 'aug2014', 'sept2014', 'oct2014', 'nov2014', 'dec2014',
              'jan2015', 'feb2015', 'mar2015', 'apr2015', 'may2015', 'jun2015', 
              'jul2015', 'aug2015', 'sept2015', 'oct2015', 'nov2015', 'dec2015',
              'jan2016', 'feb2016', 'mar2016', 'apr2016', 'may2016', 'jun2016', 
              'jul2016', 'aug2016', 'sept2016', 'oct2016', 'nov2016', 'dec2016']


n_months = (len(data_month))
n_days = (31)
n_sites = (len(df.columns))

##Create arrays for data to then check quality of:

monthly_site_data = np.zeros([n_months,n_sites,n_days])
data_monthly = np.zeros([n_months,n_sites,n_days])
#print 'shape data_monthly', np.shape(data_monthly)

##Create array for lwt data

data_monthly_lwt= np.empty([n_months,n_days])
data_monthly_lwt[:,:]=np.nan
#print 'shape yearly_monthly', np.shape(data_yearly)

##Create array of nans to put checked data in: 

data_monthly_checked = np.empty([n_months,n_sites,n_days])
data_monthly_checked[:,:,:]=np.nan


## Make lists of good data ##

good_months = [] 
good_sites = [] 


## loop through each month and select data for each month##

for i_month in range(len(data_month)):
    n_days_month = month_length[i_month]
    #print 'dates selected', data_month[i_month], month_start_look_up[i_month], month_end_look_up[i_month]
    data_month[i_month] = (df.loc[month_start_look_up[i_month]:month_end_look_up[i_month]])
    #print 'data pm', data_month[i_month]
    data_month_lwt[i_month] = (df_lwt.loc[month_start_look_up[i_month]:month_end_look_up[i_month]])
    #print 'data lwt', data_month_lwt[i_month]

## loop through sites and days within the selected monthly data ##     
    
    for i_site in range(n_sites):
        for i_day in range(len(data_month[i_month])):
            #print 'month,site,day', i_month, i_site, i_day
            #print 'data_imonth',data_month[i_month]
            temp_data = data_month[i_month].iloc[i_day,i_site]
            data_monthly[i_month,i_site,i_day] = float(temp_data)
#    for i_day in range(len(data_month[i_month])):
#        temp_data_lwt = data_month_lwt[i_month].iloc[i_day]
#        print 'td',temp_data_lwt
#        #time.sleep(1)
#        data_monthly_lwt[i_month,i_day] = float(temp_data_lwt)
#            
#print data_monthly_lwt[0,:]
#np.save('data_monthly_lwt_classification',data_monthly_lwt,allow_pickle=True, fix_imports=True)


## calculate proportion of data missing for each site during the month (number of nan's)##
 
        temp_centile_data_flattened = np.ndarray.flatten(data_monthly[i_month,i_site,:])
        #print 'imonth', i_month,'i_site', i_site, 'i_day', i_day, 'temp_array', temp_centile_data_flattened
        sorted_array = np.sort(temp_centile_data_flattened)
        #print 'sorted array', sorted_array 
        #print np.size(sorted_array)
        data_qual = (float(np.isnan(sorted_array).sum())/float(np.size(sorted_array))*100)
        #print 'dq =', data_qual
        #print 'shape before', np.shape(data_monthly)
   
     
## if more than 90% data avaialble add to list of good months and good sites ##     
        if data_qual < 10: 
            #print 'month, site',i_month, i_site
            good_sites.append(i_site)
            good_months.append(i_month)
            
            for i_day in range(len(data_month[i_month])):
                #print 'month',i_month,'site', i_site,'day', i_day
                gd_temp_data = data_monthly[i_month,i_site,i_day]
                #print 'gd_data', gd_temp_data
                data_monthly_checked[i_month,i_site,i_day] = gd_temp_data
                       
                
## get lwt info for each day and add to array    

    #for i_day in range(len(month_length[i_month])):
for i_month in range(n_months):
    #print 'Month', i_month
    for i_day in range(month_length[i_month]):
        #print (month_length[i_month])
        #print 'Iday', i_day
        temp_data_lwt = (data_month_lwt[i_month].iloc[i_day])
        #print 'data selected', temp_data_lwt  
        data_monthly_lwt[i_month,i_day] = float(temp_data_lwt)
#print '0,0',data_yearly_lwt[0,0], '0,1',data_yearly_lwt[0,1], '1,1',data_yearly_lwt[1,1]


## Check what the lists and arrays look like 
        
#print 'gm', good_months
#print 'gs', good_sites
print 'shape data', np.shape(data_monthly_checked), np.shape(data_monthly_lwt)
print 'data', data_monthly_checked[:,:,:]
print 'lwt', data_monthly_lwt[:,:]

## create empty numpy arrays to put lwt pm25 data into

NE_data = np.empty([n_months,n_sites,n_days])
NE_data[:,:,:] = np.nan
E_data = np.empty([n_months,n_sites,n_days])
E_data[:,:,:] = np.nan
SE_data = np.empty([n_months,n_sites,n_days])
SE_data[:,:,:] = np.nan
S_data = np.empty([n_months,n_sites,n_days])
S_data[:,:,:] = np.nan
SW_data = np.empty([n_months,n_sites,n_days])
SW_data[:,:,:] = np.nan
W_data = np.empty([n_months,n_sites,n_days])
W_data[:,:,:] = np.nan
NW_data = np.empty([n_months,n_sites,n_days])
NW_data[:,:,:] = np.nan
N_data = np.empty([n_months,n_sites,n_days])
N_data[:,:,:] = np.nan




## Loop through lwt array to select each lwt for all sites for each year

NE_index = [1,11,21]
E_index = [2,12,22]
SE_index = [3,13,23]
S_index = [4,14,24]
SW_index = [5,15,25]
W_index = [6,16,26]
NW_index = [7,17,27]
N_index = [8,18,28]


## Create arrays for lwt data combined and statistics/boxplots


## SPRING 


lamb_weather_type = ['N','NE','E','SE','S','SW','W','NW']
n_lwt = len(lamb_weather_type)
lwt_array = np.empty([n_lwt,n_months,n_sites,n_days])
lwt_array[:,:,:,:] = np.nan
lwt_array_summer = np.empty([n_lwt,n_months,n_sites,n_days])
lwt_array_summer[:,:,:,:] = np.nan
n_stats = 5
statistics = np.zeros([n_stats,n_lwt])
statistics_summer = np.zeros([n_stats,n_lwt])
statistics_autumn= np.zeros([n_stats,n_lwt])
statistics_winter = np.zeros([n_stats,n_lwt])



for i_month in range(len(data_month)):
    #print 'I-MONTH', i_month
    ##time.sleep(2)
    NE_flow = np.where((data_monthly_lwt[i_month,:] == NE_index[0]) | (data_monthly_lwt[i_month,:] == NE_index[1]) | (data_monthly_lwt[i_month,:] == NE_index[2]))
    E_flow = np.where((data_monthly_lwt[i_month,:] == E_index[0]) | (data_monthly_lwt[i_month,:] == E_index[1]) | (data_monthly_lwt[i_month,:] == E_index[2]))
    SE_flow = np.where((data_monthly_lwt[i_month,:] == SE_index[0]) | (data_monthly_lwt[i_month,:] == SE_index[1]) | (data_monthly_lwt[i_month,:] == SE_index[2]))
    S_flow = np.where((data_monthly_lwt[i_month,:] == S_index[0]) | (data_monthly_lwt[i_month,:] == S_index[1]) | (data_monthly_lwt[i_month,:] == S_index[2]))
    SW_flow = np.where((data_monthly_lwt[i_month,:] == SW_index[0]) | (data_monthly_lwt[i_month,:] == SW_index[1]) | (data_monthly_lwt[i_month,:] == SW_index[2]))
    W_flow = np.where((data_monthly_lwt[i_month,:] == W_index[0]) | (data_monthly_lwt[i_month,:] == W_index[1]) | (data_monthly_lwt[i_month,:] == W_index[2]))
    NW_flow = np.where((data_monthly_lwt[i_month,:] == NW_index[0]) | (data_monthly_lwt[i_month,:] == NW_index[1]) | (data_monthly_lwt[i_month,:] == NW_index[2]))
    N_flow = np.where((data_monthly_lwt[i_month,:] == N_index[0]) | (data_monthly_lwt[i_month,:] == N_index[1]) | (data_monthly_lwt[i_month,:] == N_index[2]))

    #print 'NE_flow', NE_flow, 'N_flow', N_flow
    #print 'month', i_month, 'NE_LOC',(NE_flow),'E_LOC',(E_flow), 'N_LOC',(N_flow)
    #print("NE LWT = ",data_monthly_lwt[i_month,NE_flow])


## Loop through sites and create array for each lwt with year, site & day
    
    for i_site in range(n_sites):
        #print 'I-SITE', i_site
        temp_data_NE = data_monthly_checked[i_month,i_site,NE_flow]
        #print 'data', temp_data_NE
        temp_data_E = data_monthly_checked[i_month,i_site,E_flow]
        temp_data_SE = data_monthly_checked[i_month,i_site,SE_flow]
        temp_data_S = data_monthly_checked[i_month,i_site,S_flow]
        temp_data_SW = data_monthly_checked[i_month,i_site,SW_flow]
        temp_data_W = data_monthly_checked[i_month,i_site,W_flow]
        temp_data_NW = data_monthly_checked[i_month,i_site,NW_flow]
        temp_data_N = data_monthly_checked[i_month,i_site,N_flow]
        #print 'NE',temp_data_NE, 
        #print 'NW', temp_data_NW
        
        #print 'i_month',i_month, 'i_site', i_site, temp_data_NE
        NE_data[i_month,i_site,NE_flow] = temp_data_NE
        #print 'data_array', NE_data[i_month,i_site,NE_flow]
        E_data[i_month,i_site,E_flow] = temp_data_E
        SE_data[i_month,i_site,SE_flow] = temp_data_SE
        S_data[i_month,i_site,S_flow] = temp_data_S
        SW_data[i_month,i_site,SW_flow] = temp_data_SW
        W_data[i_month,i_site,W_flow] = temp_data_W
        NW_data[i_month,i_site,NW_flow] = temp_data_NW
        N_data[i_month,i_site,N_flow] = temp_data_N
    #print 'N_data', NE_data[0,0,:]
#print 'NE_data', SE_data[:,:,:]


## Fill lwt_array with data for pm25 concs in each lwt 
        
lwt_array[0,:,:,:] = N_data[:,:,:]
lwt_array[1,:,:,:] = NE_data[:,:,:]
lwt_array[2,:,:,:] = E_data[:,:,:]
lwt_array[3,:,:,:] = SE_data[:,:,:]
lwt_array[4,:,:,:] = S_data[:,:,:]
lwt_array[5,:,:,:] = SW_data[:,:,:]
lwt_array[6,:,:,:] = W_data[:,:,:]
lwt_array[7,:,:,:] = NW_data[:,:,:]
#print 'lwt0', lwt_array[0,:,:,:]
#print 'lwt7', lwt_array[7,0:3,:,:]

#np.save('lwt_pm25_data_checked_monthly',lwt_array,allow_pickle=True, fix_imports=True)
#np.save('data_monthly_lwt_classification',data_monthly_lwt,allow_pickle=True, fix_imports=True)

print 'SPRING'
for i_lwt in range(len(lamb_weather_type)):
    start = 2
    stop = 5
    d_flattened = []
    #print 'list', d_flattened
    while start < 75:
       # for i_month in range(n_months):
        #print 'lwt = ', i_lwt, 'start', start, 'stop', stop
        flattened_array= np.ndarray.flatten(lwt_array[i_lwt,start:stop, :, :])
        d_flattened.append(flattened_array)
        #print d_flattened, len(d_flattened)
        ##time.sleep(1)
        #print len(d_flattened), d_flattened
        ##time.sleep(3)
        start = start + 12
        stop = stop + 12
    print 'lwt', lamb_weather_type[i_lwt]
    print 'non-nan', np.count_nonzero(~np.isnan(d_flattened))
    print 'len_array', np.shape(d_flattened)
    centile50 = np.nanpercentile(d_flattened, 50)
    statistics[0,i_lwt]= centile50
    print '50=', centile50
    ##time.sleep(2)
    centile25 = np.nanpercentile(d_flattened, 25)
    statistics[1,i_lwt]= centile25
    print '25=', centile25
    ##time.sleep(2)
    centile75 = np.nanpercentile(d_flattened, 75)
    statistics[2,i_lwt]= centile75
    print '75=', centile75
    ##time.sleep(2)
    centile90 = np.nanpercentile(d_flattened, 90)
    statistics[3,i_lwt]= centile90
    print '90=', centile90
    ##time.sleep(2)
    centile10 = np.nanpercentile(d_flattened, 10)
    statistics[4,i_lwt]= centile10
    print '10=', centile10
    ##time.sleep(5)
 

    
    
### SUMMER ##    
    

print 'SUMMER'
for i_lwt in range(len(lamb_weather_type)):
    start = 5
    stop = 8
    d_flattened_summer = []
    #print 'list', d_flattened_summer
    while start < 78:
       # for i_month in range(n_months):
        #print 'lwt = ', i_lwt, 'start', start, 'stop', stop
        flattened_array_summer= np.ndarray.flatten(lwt_array[i_lwt,start:stop, :, :])
        d_flattened_summer.append(flattened_array_summer)
        #print d_flattened, len(d_flattened)
        ##time.sleep(1)
        #print len(d_flattened), d_flattened
        ##time.sleep(3)
        start = start + 12
        stop = stop + 12
    print 'lwt', lamb_weather_type[i_lwt]
    print 'non-nan', np.count_nonzero(~np.isnan(d_flattened_summer))
    print 'len_array', np.shape(d_flattened_summer)
    #time.sleep(10)
    centile50 = np.nanpercentile(d_flattened_summer, 50)
    statistics_summer[0,i_lwt]= centile50
    print '50=', centile50
    ##time.sleep(2)
    centile25 = np.nanpercentile(d_flattened_summer, 25)
    statistics_summer[1,i_lwt]= centile25
    print '25=', centile25
    ##time.sleep(2)
    centile75 = np.nanpercentile(d_flattened_summer, 75)
    statistics_summer[2,i_lwt]= centile75
    print '75=', centile75
    ##time.sleep(2)
    centile90 = np.nanpercentile(d_flattened_summer, 90)
    statistics_summer[3,i_lwt]= centile90
    print '90=', centile90
    ##time.sleep(2)
    centile10 = np.nanpercentile(d_flattened_summer, 10)
    statistics_summer[4,i_lwt]= centile10
    print '10=', centile10
    ##time.sleep(5)
    #time.sleep(10)
    
    
## AUTUMN 
print 'AUTUMN'
for i_lwt in range(len(lamb_weather_type)):
    start = 8
    stop = 11
    d_flattened_autumn = []
    #print 'list', d_flattened_autumn
    while start < 80:
       # for i_month in range(n_months):
        #print 'lwt = ', i_lwt, 'start', start, 'stop', stop
        flattened_array_autumn= np.ndarray.flatten(lwt_array[i_lwt,start:stop, :, :])
        d_flattened_autumn.append(flattened_array_autumn)
        #print d_flattened, len(d_flattened)
        ##time.sleep(1)
        #print len(d_flattened), d_flattened
        ##time.sleep(3)
        start = start + 12
        stop = stop + 12
    print 'lwt', lamb_weather_type[i_lwt]
    print 'non-nan', np.count_nonzero(~np.isnan(d_flattened_autumn))
    print 'len_array', np.shape(d_flattened_autumn)
    #time.sleep(10)
    centile50 = np.nanpercentile(d_flattened_autumn, 50)
    statistics_autumn[0,i_lwt]= centile50
    print '50=', centile50
    ##time.sleep(2)
    centile25 = np.nanpercentile(d_flattened_autumn, 25)
    statistics_autumn[1,i_lwt]= centile25
    print '25=', centile25
    ##time.sleep(2)
    centile75 = np.nanpercentile(d_flattened_autumn, 75)
    statistics_autumn[2,i_lwt]= centile75
    print '75=', centile75
    ##time.sleep(2)
    centile90 = np.nanpercentile(d_flattened_autumn, 90)
    statistics_autumn[3,i_lwt]= centile90
    print '90=', centile90
    ##time.sleep(2)
    centile10 = np.nanpercentile(d_flattened_autumn, 10)
    statistics_autumn[4,i_lwt]= centile10
    print '10=', centile10
    ##time.sleep(5)
    #time.sleep(10)
    
  
    ## WINTER

print 'WINTER' 
for i_lwt in range(len(lamb_weather_type)):
    start = 11
    stop = 14
    d_flattened_winter = []
    #print 'list', d_flattened_winter
    while start < 83:
       # for i_month in range(n_months):
        #print 'lwt = ', i_lwt, 'start', start, 'stop', stop
        if start == 83:
            flattened_array_winter= np.ndarray.flatten(lwt_array[i_lwt,start:84, :, :])  
        else:
            flattened_array_winter= np.ndarray.flatten(lwt_array[i_lwt,start:stop, :, :])
            d_flattened_winter.append(flattened_array_winter)
            #print d_flattened, len(d_flattened)
            ##time.sleep(1)
            #print len(d_flattened), d_flattened
            ##time.sleep(3)
            start = start + 12
            stop = stop + 12
    print 'lwt', lamb_weather_type[i_lwt]
    print 'non-nan', np.count_nonzero(~np.isnan(d_flattened_winter))
    print 'len_array', np.shape(d_flattened_winter)
    time.sleep(2)
    centile50 = np.nanpercentile(d_flattened_winter, 50)
    statistics_winter[0,i_lwt]= centile50
    print '50=', centile50
    ##time.sleep(2)
    centile25 = np.nanpercentile(d_flattened_winter, 25)
    statistics_winter[1,i_lwt]= centile25
    print '25=', centile25
    ##time.sleep(2)
    centile75 = np.nanpercentile(d_flattened_winter, 75)
    statistics_winter[2,i_lwt]= centile75
    print '75=', centile75
    ##time.sleep(2)
    centile90 = np.nanpercentile(d_flattened_winter, 90)
    statistics_winter[3,i_lwt]= centile90
    print '90=', centile90
    ##time.sleep(2)
    centile10 = np.nanpercentile(d_flattened_winter, 10)
    statistics_winter[4,i_lwt]= centile10
    print '10=', centile10
    ##time.sleep(5)
    #time.sleep(10)
    
offset = 0.3
lwt_val = [0,1,2,3,4,5,6,7]

fig = plt.figure(figsize=(10,8))
fig, (ax0, ax1) = plt.subplots(2, sharex=True, sharey=True)
for i in range(n_lwt):   

    ax0.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[0,i],statistics[0,i]], 'r-') 
    ax0.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[1,i],statistics[1,i]], 'b-')
    ax0.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[2,i],statistics[2,i]], 'b-')
    ax0.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[4,i],statistics[4,i]], 'b-')
    ax0.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[3,i],statistics[3,i]], 'b-')
    ax0.plot([lwt_val[i]-offset,lwt_val[i]-offset],[statistics[1,i],statistics[2,i]], 'b-')
    ax0.plot([lwt_val[i]+offset,lwt_val[i]+offset],[statistics[1,i],statistics[2,i]], 'b-')
    ax0.plot([lwt_val[i],lwt_val[i]],[statistics[4,i],statistics[1,i]], 'b-')
    ax0.plot([lwt_val[i],lwt_val[i]],[statistics[2,i],statistics[3,i]], 'b-')

    ax1.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics_summer[0,i],statistics_summer[0,i]], 'r-') 
    ax1.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics_summer[1,i],statistics_summer[1,i]], 'b-')
    ax1.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics_summer[2,i],statistics_summer[2,i]], 'b-')
    ax1.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics_summer[4,i],statistics_summer[4,i]], 'b-')
    ax1.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics_summer[3,i],statistics_summer[3,i]], 'b-')
    ax1.plot([lwt_val[i]-offset,lwt_val[i]-offset],[statistics_summer[1,i],statistics_summer[2,i]], 'b-')
    ax1.plot([lwt_val[i]+offset,lwt_val[i]+offset],[statistics_summer[1,i],statistics_summer[2,i]], 'b-')
    ax1.plot([lwt_val[i],lwt_val[i]],[statistics_summer[4,i],statistics_summer[1,i]], 'b-')
    ax1.plot([lwt_val[i],lwt_val[i]],[statistics_summer[2,i],statistics_summer[3,i]], 'b-')
    
    

labels0 = [ 'N','NE','E','SE','S','SW','W','NW']
labels1 = [ 'N','NE','E','SE','S','SW','W','NW' ]
ax0.set_xlim((-1,8))
ax0.set_ylim((0,50))
ax1.set_xlim((-1,8))
ax1.set_ylim((0,50))
#ax0.set_xticks(lwt_val0, labels0)
#ax1.set_xticks(lwt_val1,labels1)
plt.xticks(lwt_val, labels0)
ax0.set_title('PM$_{2.5}$ Concentrations & LWT 2010-2016 Background \n Spring ')
ax0.set_ylabel('PM$_{2.5}$ Concentration')
ax1.set_title('Summer')
ax1.set_ylabel('PM$_{2.5}$ Concentration')
#ax0.set_xlabel('Lamb Weather Type')
ax1.set_xlabel('Lamb Weather Type')
plt.savefig('monthly_check_lwt_seasonal_spring_summer.png')
plt.show()



offset = 0.3
lwt_val = [0,1,2,3,4,5,6,7]

fig = plt.figure(figsize=(10,8))
fig, (ax0, ax1) = plt.subplots(2, sharex=True, sharey=True)
for i in range(n_lwt):   

    ax0.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics_autumn[0,i],statistics_autumn[0,i]], 'r-') 
    ax0.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics_autumn[1,i],statistics_autumn[1,i]], 'b-')
    ax0.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics_autumn[2,i],statistics_autumn[2,i]], 'b-')
    ax0.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics_autumn[4,i],statistics_autumn[4,i]], 'b-')
    ax0.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics_autumn[3,i],statistics_autumn[3,i]], 'b-')
    ax0.plot([lwt_val[i]-offset,lwt_val[i]-offset],[statistics_autumn[1,i],statistics_autumn[2,i]], 'b-')
    ax0.plot([lwt_val[i]+offset,lwt_val[i]+offset],[statistics_autumn[1,i],statistics_autumn[2,i]], 'b-')
    ax0.plot([lwt_val[i],lwt_val[i]],[statistics_autumn[4,i],statistics_autumn[1,i]], 'b-')
    ax0.plot([lwt_val[i],lwt_val[i]],[statistics_autumn[2,i],statistics_autumn[3,i]], 'b-')

    ax1.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics_winter[0,i],statistics_winter[0,i]], 'r-') 
    ax1.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics_winter[1,i],statistics_winter[1,i]], 'b-')
    ax1.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics_winter[2,i],statistics_winter[2,i]], 'b-')
    ax1.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics_winter[4,i],statistics_winter[4,i]], 'b-')
    ax1.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics_winter[3,i],statistics_winter[3,i]], 'b-')
    ax1.plot([lwt_val[i]-offset,lwt_val[i]-offset],[statistics_winter[1,i],statistics_winter[2,i]], 'b-')
    ax1.plot([lwt_val[i]+offset,lwt_val[i]+offset],[statistics_winter[1,i],statistics_winter[2,i]], 'b-')
    ax1.plot([lwt_val[i],lwt_val[i]],[statistics_winter[4,i],statistics_winter[1,i]], 'b-')
    ax1.plot([lwt_val[i],lwt_val[i]],[statistics_winter[2,i],statistics_winter[3,i]], 'b-')
    
    

labels0 = [ 'N','NE','E','SE','S','SW','W','NW' ]
labels1 = [ 'N','NE','E','SE','S','SW','W','NW' ]
ax0.set_xlim((-1,8))
ax0.set_ylim((0,50))
ax1.set_xlim((-1,8))
ax1.set_ylim((0,50))
#ax0.set_xticks(lwt_val0, labels0)
#ax1.set_xticks(lwt_val1,labels1)
plt.xticks(lwt_val, labels0)
ax0.set_title('PM$_{2.5}$ Concentrations & LWT 2010-2016 Background \n Autumn  ')
ax0.set_ylabel('PM$_{2.5}$ Concentration')
ax1.set_title('Winter ')
ax1.set_ylabel('PM$_{2.5}$ Concentration')
#ax0.set_xlabel('Lamb Weather Type')
ax1.set_xlabel('Lamb Weather Type')
plt.savefig('monthly_check_lwt_seasonal_autumn_winter.png')
plt.show()




#
#
#offset = 0.3
#lwt_val = [0,1,2,3,4,5,6,7]
#
#fig = plt.figure(figsize=(10,8))
#ax = fig.add_subplot(111)
#for i in range(n_lwt):   
#
##    plt.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[0,i],statistics[0,i]], 'r-') 
##    plt.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[1,i],statistics[1,i]], 'b-')
##    plt.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[2,i],statistics[2,i]], 'b-')
##    plt.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[4,i],statistics[4,i]], 'b-')
##    plt.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[3,i],statistics[3,i]], 'b-')
##    plt.plot([lwt_val[i]-offset,lwt_val[i]-offset],[statistics[1,i],statistics[2,i]], 'b-')
##    plt.plot([lwt_val[i]+offset,lwt_val[i]+offset],[statistics[1,i],statistics[2,i]], 'b-')
##    plt.plot([lwt_val[i],lwt_val[i]],[statistics[4,i],statistics[1,i]], 'b-')
##    plt.plot([lwt_val[i],lwt_val[i]],[statistics[2,i],statistics[3,i]], 'b-')
#
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
#
#labels = [ 'N','NE','E','SE','S','SW','W','NW' ]
#ax.set_xlim((-1,8))
#ax.set_ylim((0,70))
#
#plt.xticks(lwt_val, labels)
#ax.set_title('Spring PM$_{2.5}$ Concentrations & LWT 2010-2016 \n Background ')
#ax.set_ylabel('PM$_{2.5}$ Concentration')
#ax.set_xlabel('Lamb Weather Type')
#plt.savefig('test_data_qual_lwt_spring_monthly.png')
#plt.show()
#
#
#
#
#
