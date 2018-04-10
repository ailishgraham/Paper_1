#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:55:09 2018

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


df = pd.read_csv("/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/pm25_rural_data/pm25.csv",parse_dates=[0],usecols=[0,9,10,11,12,13,14,15,16,17,18,19,20,
                                         21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52])
df_lwt = pd.read_csv("/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/pm25_rural_data/pm25.csv",usecols=[0,8])
#print df.head()
#print df_lwt.head()

#Replace Date String with Datetime and set as index
df = df.replace('No data', np.NaN)
df['Date'] = pd.to_datetime(df['Date'])
#print 'datetype', type(date)
#print df['Date'], type(df['Date']),np.shape(df['Date']), len(df['Date'])
df = df.set_index(['Date'])

# Set Date as index in LWT dataframe 
df_lwt['Date'] = pd.to_datetime(df_lwt['Date'])
df_lwt = df_lwt.set_index(['Date'])

## Dates to loop over ##

data_year = ['2010', '2011', '2012', '2013', '2014', '2015', '2016']

year_start_look_up = ['2010-01-01', '2011-01-01', '2012-01-01', '2013-01-01',
                       '2014-01-01', '2015-01-01', '2016-01-01']

year_end_look_up = ['2010-12-31', '2011-12-31', '2012-12-31', '2013-12-31',
                     '2014-12-31','2015-12-31','2016-12-31']

data_year_lwt = ['2010', '2011', '2012', '2013', '2014', '2015', '2016']


# Set dimensions of array
n_years = (len(data_year))
n_days = (365)
n_sites = (len(df.columns))
#ßprint 'n_years', n_years,'n_days', n_days,'n_sites', n_sites 


#Create arrays for data to then check quality of:
yearly_site_data = np.zeros([n_years,n_sites,n_days])
data_yearly = np.zeros([n_years,n_sites,n_days])


#Create array for lwt data
data_yearly_lwt= np.zeros([n_years,n_days])
#print 'shape yearly_monthly', np.shape(data_yearly)


#Create array of nans to put checked data in: 
data_yearly_checked = np.empty([n_years,n_sites,n_days])
data_yearly_checked[:,:,:]=np.nan


## Make lists of good data ##
good_years = [] 
good_sites = [] 


## loop through each year and select data for each year##
for i_year in range(len(data_year)):
    #print 'Iyear', i_year, 'len_yr', year_length[i_year]
    #print 'dates selected', data_year[i_year], date_start_look_up[i_year], date_end_look_up[i_year]
    data_year[i_year] = (df.loc[year_start_look_up[i_year]:year_end_look_up[i_year]])
    #print 'len_data', len(data_year[i_year]), 'data_year = ', data_year[i_year]
    #print data_year_lwt[i_year]
    data_year_lwt[i_year]= (df_lwt.loc[year_start_look_up[i_year]:year_end_look_up[i_year]])

## loop through sites and days within the selected monthly data ##     
    
    for i_site in range(n_sites):
        for i_day in range(n_days):
            #print 'len_year', range(n_days)
            #print 'year,site,day', i_year, i_site, i_day
            #print 'data_imonth',data_month[i_month]
            temp_data = (data_year[i_year].iloc[i_day,i_site])
            #print 'data selected', temp_data
            data_yearly[i_year,i_site,i_day] = float(temp_data)
#print data_yearly[:,:,:]
#time.sleep(10)
            

    
## calculate proportion of data missing for each site during the month (number of nan's)##
       
        temp_centile_data_flattened = np.ndarray.flatten(data_yearly[i_year,i_site,:])
        sorted_array = np.sort(temp_centile_data_flattened)
        #print 'sorted array', sorted_array, 'year', i_year, 'site', i_site,
        data_qual = (float(np.isnan(sorted_array).sum())/float(np.size(sorted_array))*100)
        #print 'dq =', data_qual
   
    
## if more than 90% data avaialble add to list of good months and good sites ##     
       
        if data_qual < 10:    
            #print('year, site', i_year, i_site)
            #print('dq', data_qual)
            #time.sleep(1)
            #print 'year, site', i_year, i_site
            #print 'array', temp_centile_data_flattened
            good_sites.append(i_site)
            good_years.append(i_year)
            for i_day in range(n_days):
                #print('year',i_year,'site', i_site,'day', i_day)
                gd_temp_data = data_yearly[i_year,i_site,i_day]
                #print 'gd_data', gd_temp_data
                data_yearly_checked[i_year,i_site,i_day] = gd_temp_data
#print('len gs',len(good_sites))
#print(good_sites)
#time.sleep(10)
#print('len gy',len(good_years))
#print data_yearly_checked[:,:,:]        
#time.sleep(10)

## get lwt info for each day and add to array    

    for i_day in range(n_days):
        temp_data_lwt = (data_year_lwt[i_year].iloc[i_day])
        #print 'data selected', temp_data_lwt 
        data_yearly_lwt[i_year,i_day] = float(temp_data_lwt)
#print '0,0',data_yearly_lwt[0,0], '0,1',data_yearly_lwt[0,1], '1,1',data_yearly_lwt[1,1]
#time.sleep(10)
    
## Check what the lists and arrays look like 
        
#print 'gy', good_years
#print 'gs', good_sites
#print 'shape data', np.shape(data_yearly_checked), 'shape lwt', np.shape(data_yearly_lwt)
#print 'data', data_yearly_checked[:,:,:]
#print 'lwt', data_yearly_lwt[:,:]

## create empty numpy arrays to put lwt pm25 data into

NE_data = np.empty([n_years,n_sites,n_days])
NE_data[:,:,:] = np.nan
E_data = np.empty([n_years,n_sites,n_days])
E_data[:,:,:] = np.nan
SE_data = np.empty([n_years,n_sites,n_days])
SE_data[:,:,:] = np.nan
S_data = np.empty([n_years,n_sites,n_days])
S_data[:,:,:] = np.nan
SW_data = np.empty([n_years,n_sites,n_days])
SW_data[:,:,:] = np.nan
W_data = np.empty([n_years,n_sites,n_days])
W_data[:,:,:] = np.nan
NW_data = np.empty([n_years,n_sites,n_days])
NW_data[:,:,:] = np.nan
N_data = np.empty([n_years,n_sites,n_days])
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

lamb_weather_type = ['N','NE','E','SE','S','SW','W','NW']
n_lwt = len(lamb_weather_type)
lwt_array = np.empty([n_lwt,n_years,n_sites,n_days])
lwt_array[:,:,:,:] = np.nan
n_stats = 5
statistics = np.zeros([n_stats,n_lwt])

for i_year in range(len(data_year)):
    NE_flow = np.where((data_yearly_lwt[i_year,:] == NE_index[0]) | (data_yearly_lwt[i_year,:] == NE_index[1]) | (data_yearly_lwt[i_year,:] == NE_index[2]))
    E_flow = np.where((data_yearly_lwt[i_year,:] == E_index[0]) | (data_yearly_lwt[i_year,:] == E_index[1]) | (data_yearly_lwt[i_year,:] == E_index[2]))
    SE_flow = np.where((data_yearly_lwt[i_year,:] == SE_index[0]) | (data_yearly_lwt[i_year,:] == SE_index[1]) | (data_yearly_lwt[i_year,:] == SE_index[2]))
    S_flow = np.where((data_yearly_lwt[i_year,:] == S_index[0]) | (data_yearly_lwt[i_year,:] == S_index[1]) | (data_yearly_lwt[i_year,:] == S_index[2]))
    SW_flow = np.where((data_yearly_lwt[i_year,:] == SW_index[0]) | (data_yearly_lwt[i_year,:] == SW_index[1]) | (data_yearly_lwt[i_year,:] == SW_index[2]))
    W_flow = np.where((data_yearly_lwt[i_year,:] == W_index[0]) | (data_yearly_lwt[i_year,:] == W_index[1]) | (data_yearly_lwt[i_year,:] == W_index[2]))
    NW_flow = np.where((data_yearly_lwt[i_year,:] == NW_index[0]) | (data_yearly_lwt[i_year,:] == NW_index[1]) | (data_yearly_lwt[i_year,:] == NW_index[2]))
    N_flow = np.where((data_yearly_lwt[i_year,:] == N_index[0]) | (data_yearly_lwt[i_year,:] == N_index[1]) | (data_yearly_lwt[i_year,:] == N_index[2]))

    #print 'SE_flow', SE_flow
    #print 'year', i_year, 'NE_LOC',(NE_flow),'E_LOC',(E_flow), 'N_LOC',(N_flow)
#    print("NE LWT = ",data_yearly_lwt[i_year,NE_flow])
#    time.sleep(5)
    #print 'nosites', data_yearly_checked[i_year,:,NE_flow]

## Loop through sites and create array for each lwt with year, site & day
    
    for i_site in range(n_sites):
        temp_data_NE = data_yearly_checked[i_year,i_site,NE_flow]
        temp_data_E = data_yearly_checked[i_year,i_site,E_flow]
        temp_data_SE = data_yearly_checked[i_year,i_site,SE_flow]
        temp_data_S = data_yearly_checked[i_year,i_site,S_flow]
        temp_data_SW = data_yearly_checked[i_year,i_site,SW_flow]
        temp_data_W = data_yearly_checked[i_year,i_site,W_flow]
        temp_data_NW = data_yearly_checked[i_year,i_site,NW_flow]
        temp_data_N = data_yearly_checked[i_year,i_site,N_flow]
        
        #print 'i_year',i_year, 'i_site', i_site, temp_data_NE
        NE_data[i_year,i_site,NE_flow] = temp_data_NE
        E_data[i_year,i_site,E_flow] = temp_data_E
        SE_data[i_year,i_site,SE_flow] = temp_data_SE
        S_data[i_year,i_site,S_flow] = temp_data_S
        SW_data[i_year,i_site,SW_flow] = temp_data_SW
        W_data[i_year,i_site,W_flow] = temp_data_W
        NW_data[i_year,i_site,NW_flow] = temp_data_NW
        N_data[i_year,i_site,N_flow] = temp_data_N
#print 'N_data', N_data[:,:,:]
#print 'SE_data', SE_data[:,:,:]
#print 'SW_data', SW_data[:,:,:]
#time.sleep(100)

## Fill lwt_array with data for pm25 concs in each lwt 
        
lwt_array[0,:,:,:] = N_data[:,:,:]
lwt_array[1,:,:,:] = NE_data[:,:,:]
lwt_array[2,:,:,:] = E_data[:,:,:]
lwt_array[3,:,:,:] = SE_data[:,:,:]
lwt_array[4,:,:,:] = S_data[:,:,:]
lwt_array[5,:,:,:] = SW_data[:,:,:]
lwt_array[6,:,:,:] = W_data[:,:,:]
lwt_array[7,:,:,:] = NW_data[:,:,:]

#np.save('lwt_pm25_data_checked', lwt_array, allow_pickle=True, fix_imports=True)
#print lwt_array[7,:,:,:]


for i_lwt in range(len(lamb_weather_type)):
    #print 'lwt', i_lwt
    d_flattened = np.ndarray.flatten(lwt_array[i_lwt,:, :, :])
    #print 'i_year', i_year, 
    #print 'd flat', d_flattened
    #time.sleep(5)
    
    #    centile10 = np.nanpercentile(d_flattened, 10)
    #    statistics[4,lwt]= centile10
    
    centile50 = np.nanpercentile(d_flattened, 50)
    statistics[0,i_lwt]= centile50
    #print '50=', centile50
    #time.sleep(2)
    centile25 = np.nanpercentile(d_flattened, 25)
    statistics[1,i_lwt]= centile25
    #print '25=', centile25
    #time.sleep(2)
    centile75 = np.nanpercentile(d_flattened, 75)
    statistics[2,i_lwt]= centile75
    #print '75=', centile75
    #time.sleep(2)
    centile90 = np.nanpercentile(d_flattened, 90)
    statistics[3,i_lwt]= centile90
    #print '90=', centile90
    #time.sleep(2)
    centile10 = np.nanpercentile(d_flattened, 10)
    statistics[4,i_lwt]= centile10
    #print '10=', centile10
    #time.sleep(5)
    


offset = 0.3
lwt_val = [0,1,2,3,4,5,6,7]

fig = plt.figure(figsize=(12,4))
ax = fig.add_subplot(111)
for i in range(n_lwt):   

#    plt.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[0,i],statistics[0,i]], 'r-') 
#    plt.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[1,i],statistics[1,i]], 'b-')
#    plt.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[2,i],statistics[2,i]], 'b-')
#    plt.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[4,i],statistics[4,i]], 'b-')
#    plt.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[3,i],statistics[3,i]], 'b-')
#    plt.plot([lwt_val[i]-offset,lwt_val[i]-offset],[statistics[1,i],statistics[2,i]], 'b-')
#    plt.plot([lwt_val[i]+offset,lwt_val[i]+offset],[statistics[1,i],statistics[2,i]], 'b-')
#    plt.plot([lwt_val[i],lwt_val[i]],[statistics[4,i],statistics[1,i]], 'b-')
#    plt.plot([lwt_val[i],lwt_val[i]],[statistics[2,i],statistics[3,i]], 'b-')

    
    ax.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[0,i],statistics[0,i]], 'r-') 
    ax.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[1,i],statistics[1,i]], 'b-')
    ax.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[2,i],statistics[2,i]], 'b-')
    ax.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[4,i],statistics[4,i]], 'b-')
    ax.plot([lwt_val[i]-offset,lwt_val[i]+offset],[statistics[3,i],statistics[3,i]], 'b-')
    ax.plot([lwt_val[i]-offset,lwt_val[i]-offset],[statistics[1,i],statistics[2,i]], 'b-')
    ax.plot([lwt_val[i]+offset,lwt_val[i]+offset],[statistics[1,i],statistics[2,i]], 'b-')
    ax.plot([lwt_val[i],lwt_val[i]],[statistics[4,i],statistics[1,i]], 'b-')
    ax.plot([lwt_val[i],lwt_val[i]],[statistics[2,i],statistics[3,i]], 'b-')

labels = [ 'N','NE','E','SE','S','SW','W','NW' ]
ax.set_xlim((-1,8))
ax.set_ylim((0,50))

plt.xticks(lwt_val, labels)
ax.set_title('Annual PM$_{2.5}$ Concentrations & LWT 2010-2016 \n Background ')
ax.set_ylabel('PM$_{2.5}$ Concentration')
ax.set_xlabel('Lamb Weather Type')
plt.savefig('pm25_lwt_annual_data_check.png')
plt.show()









####  THEN MAKE A CORRELAION MATRIX ##
##
##for i_month in range(len(data_month)):
###    coreff = np.corrcoef(monthly_site_data[i_month,0,0],monthly_site_data[i_month,0,1])
###    print coreff
##    for i_site in range(n_sites):
##        while i_site <= 43:
##            coreff = np.corrcoef(monthly_site_data[i_month,i_site,:],monthly_site_data[i_month,i_site+1,:])
##            print coreff

