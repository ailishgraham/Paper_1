#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:18:58 2018

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
import math


df = pd.read_csv("/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/pm25_rural_data/pm25.csv", usecols=[0,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                         21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52])
#print 'df bf', df

# Replace old headers of site names with latitude of each site
old_header = ('Date', 'LWT', 'Aberdeen', 'Auchencorth Moss', 
              'Belfast Centre', 'Birmingham Acocks Green', 
              'Blackpool 03ton', "Bristol St Paul's", 'Cardiff Centre', 
              'Chesterfield Loundsley Green', 'Chilbolton Observatory', 
              'Coventry Allesley', 'Derry Rosemount', 'Eastbourne', 
              'Edinburgh St Leonards', 'Glasgow Townhead', 'Hull Freetown',
              'Leamington Spa', 'Leeds Centre', 'Leicester University', 
              'London Bexley', 'London Bloomsbury', 'London Eltham',
              'London Harrow Stanmore', 'London N. Kensington', 
              'London Teddington Bushy Park', 'Manchester Piccadilly', 
              'Newcastle Centre', 'Newport', 'Norwich Lakenfields', 
              'Nottingham Centre', 'Oxford St Ebbes', 'Plymouth Centre',
              'Portsmouth', 'Preston', 'Reading New Town', 'Rochester Stoke',
              'Salford Eccles', 'Sheffield Devonshire Green', 
              'Southampton Centre', 'Southend-on-Sea', 'Stoke-on-Trent Centre', 
              'Sunderland Silksworth', 'Wigan Centre', 'Wirral Tranmere', 
              'York Bootham')
new_header = ('Date', 'LWT','57.15736','55.79216','54.59965','51.45258','53.80489',
        '51.462839','51.48178','53.244131','51.149617','52.411563','55.002818',
        '50.805778','55.945589','55.865782','53.74878','52.28881','53.80378',
        '52.619823','51.46603','51.52229','51.45258','51.617333','51.52105',
        '51.425286','53.48152','54.97825','51.601203','52.614193','52.95473',
        '51.744806','50.37167','50.82881','53.76559','51.45309','51.45617',
        '53.48481','53.378622','50.90814','51.544206','53.02821','54.88361',
        '53.54914','53.37287','53.967513')
col_rename_dict = {i:j for i,j in zip(old_header,new_header)}
df.rename(columns=col_rename_dict, inplace=True)
#print 'df aft', df

#Replace Date String with Datetime
df['Date'] = pd.to_datetime(df['Date'])
date = df['Date']
#print date, date[0], date[1]

# Select only the data rows (not date and LWT)
data = df.iloc[:, 2:]
data = data.replace('No data', np.NaN)
#print 'nandata', data


######## Create arrays and Read in data ###########

##################
# 1st array n_days by n_sites
##################

n_sites = (len(data.columns))
#print n_sites
n_days = (len(data.index))
#print i_days
cluster_data_day = np.zeros([n_days, n_sites])
#print 'day.shape',cluster_data_day.shape

for i_site in range(n_days):
    for i_day in range(n_sites):
#        print 'len rows', len(data.index)
#        print 'len cols', len(data.columns)
        temp_data = data.iloc[i_site,i_day]
        cluster_data_day[i_site,i_day] = float(temp_data)
#print cluster_data_day[:,:]
#print np.shape(cluster_data_day)


##################
# 2nd array n_sites by n_days 
##################

n_sites = (len(data.columns))
#print n_sites
n_days = (len(data.index))
#print n_days
cluster_data_site = np.zeros([n_sites,n_days])
print 'site.shape', cluster_data_site.shape

for i_site in range(n_sites):
    for i_day in range(n_days):
#        print 'len rows', len(data.index)
#        print 'len cols', len(data.columns)
        temp_data = data.iloc[i_day,i_site]
        cluster_data_site[i_site,i_day] = float(temp_data)
#print cluster_data_site[:,:]
#print np.shape(cluster_data_site)

################# end of array creation ##################


######### PLOT data to check values #########

#for i_day in range(n_days): 
#    x = date[i_day]
#    print x
#    for i_site in range(n_sites):
#        y = cluster_data_day[i_day,i_site]
#        print y
#        plt.scatter(x,y)
#plt.xlim(date.min(), date.max())
#plt.ylim(0, 100)
#plt.xlabel('Year')
#plt.ylabel('PM$_{2.5}$ concentration')
#plt.title('Mean Daily Rural PM$_{2.5}$ Concentration 2010-2016')
#plt.savefig('rural_pm25.png')
#plt.show()


########## END OF PLOT CHECK ###############


#### Pick sites with good data availability (>85% availability) ####

good_sites = []

## calculate data quality for each site ##

for i_site in range(n_sites):
    temp_centile_data_flattened = np.ndarray.flatten(cluster_data_site[i_site,:])
    #print temp_centile_data_flattened
    sorted_array = np.sort(temp_centile_data_flattened)
    #print np.size(sorted_array)
    data_qual = (float(np.isnan(sorted_array).sum())/float(np.size(sorted_array))*100)
    print 'dq',data_qual, i_site

## If data availability >85% add to list of good sites ##

    if data_qual < 15: 
        print 'good dq',i_site
        good_sites.append(i_site)
print good_sites
#print len(good_sites)


## Create array of good sites and add data from good sites to it ##

n_gd_sites = len(good_sites)
good_data_sites = np.zeros([n_gd_sites,n_days])
n_stats = 4
stats_sites = np.zeros([n_stats, n_gd_sites])

for index in range(len(good_sites)):
    #print index, good_sites[index]
    temp_data = cluster_data_site[good_sites[index], :]
    good_data_sites[index,:] = temp_data
    print good_data_sites[index,:]
#print good_data_sites[0,:]
#print cluster_data_site[0,:]
print 'shape good sites', np.shape(good_data_sites)

## Loop through good sites to order data in ascending values ##

for i_site in range(len(good_sites)):
    #print 'gd_data_array',good_data_sites[i_site,:]
    #print 'dq', (float(np.isnan(good_data_sites[i_site,:]).sum()))
    sorted_array = np.sort(good_data_sites[i_site,:])
    sorted_array_nan = sorted_array[np.logical_not(np.isnan(sorted_array))]
    print 'site', i_site, 'array', sorted_array_nan
    #print 'sorted_nan', len(sorted_array_nan)

## Calculate the 5th,10th,90th and 95th % of data and calculate mean of each
## Then add to stats_sites array ##

    len_array= float(len(sorted_array_nan))
#    print 'sites.len', len_array
    ninety_index=(int(math.floor(len_array)*0.9))
    ninetyfive_index=(int(math.floor(len_array)*0.95))
    ten_index = (int(math.floor(len_array)*0.1))
    five_index = (int(math.floor(len_array)*0.05))
#    print '90index', ninety_index, i_site
#    print'95index', ninetyfive_index, i_site
#    print '10index', ten_index, i_site
#    print '5index', five_index, i_site
    ninety_values = sorted_array_nan[ninety_index:len_array]
    ninetyfive_values = sorted_array_nan[ninetyfive_index:len_array]
    ten_values = sorted_array_nan[0:ten_index]   
    five_values = sorted_array_nan[0:five_index] 
    #print '90,95,10,5',ninety_values, ninetyfive_values, ten_values, five_values

    meancentile90 = np.nanmean(ninety_values)
#    print 'mean90', meancentile90
    meancentile95 = np.nanmean(ninetyfive_values)
#    print 'mean95', meancentile95
    meancentile10 = np.nanmean(ten_values)
#    print 'mean10', meancentile10
    meancentile5 = np.nanmean(five_values)
#    print 'mean5', meancentile5

    stats_sites[0,i_site]= meancentile5 
    stats_sites[1,i_site]= meancentile10
    stats_sites[2,i_site]= meancentile90 
    stats_sites[3,i_site]= meancentile95
print '5sites',stats_sites[0,:]
print '10sites',stats_sites[1,:]
print '90sites',stats_sites[2,:]
print '95sites',stats_sites[3,:]


## Repeat above loop for days (instead of sites) ##

good_data_days = np.zeros([n_gd_sites,n_days])
stats_days = np.zeros([n_stats, n_days])

for i_day in range(n_days):
    sorted_array_days=np.sort(good_data_sites[:,i_day])
#    print i_day, sorted_array_days
    sorted_array_days_nan = sorted_array_days[np.logical_not(np.isnan(sorted_array_days))]
    print 'day', 'i_day', sorted_array_days_nan
    len_array_days= float(len(sorted_array_days_nan))
#    print 'sites.len', len_array
    ninety_index_days=(int(math.floor(len_array_days)*0.9))
    ninetyfive_index_days=(int(math.floor(len_array_days)*0.95))
    ten_index_days=(int(math.floor(len_array_days)*0.1))
    five_index_days=(int(math.floor(len_array_days)*0.05))
#    print '90=',ninety_index_days, '95=',ninetyfive_index_days,
#    '10=', ten_index_days, '5=', five_index_days
    
    ninety_values_days = sorted_array_days_nan[ninety_index_days:len_array_days]
    ninetyfive_values_days = sorted_array_days_nan[ninetyfive_index_days:len_array_days]
    ten_values_days = sorted_array_days_nan[0:ten_index_days]   
    five_values_days = sorted_array_days_nan[0:five_index_days] 
    #print '90,95,10,5',ninety_values, ninetyfive_values, ten_values, five_values
    meancentile90_days = np.nanmean(ninety_values_days)
    print 'mean90days', meancentile90_days
    meancentile95_days = np.nanmean(ninetyfive_values_days)
    print 'mean95days', meancentile95_days
    meancentile10_days = np.nanmean(ten_values_days)
    print 'mean10days', meancentile10_days
    meancentile5_days = np.nanmean(five_values_days)
    print 'mean5days', meancentile5_days
    
    
    stats_days[0,i_day]= meancentile5_days
    stats_days[1,i_day]= meancentile10_days
    stats_days[2,i_day]= meancentile90_days
    stats_days[3,i_day]= meancentile95_days
print '5days',stats_days[0,:]
print '10days',stats_days[1,:]
print '90days',stats_days[2,:]
print '95days',stats_days[3,:]


## Check shape of each of the stats arrays ##

print 'days', np.shape(stats_days)
print 'sites', np.shape(stats_sites)


## Create plots of these stats against site/day ##

## PLOT OF SITES ##


for i_site in range(n_gd_sites): 
    y = stats_sites[2,i_site]
    #print y
    for i_day in range(n_days):
        x = date[i_day]
        #print x
        plt.scatter(x,y)
plt.xlim(date.min(), date.max())
plt.ylim(0, 100)
plt.xlabel('Year')
plt.ylabel('PM$_{2.5}$ concentration')
plt.title('Mean Site 90th centile Rural PM$_{2.5}$ Concentration 2010-2016')
plt.savefig('gdsites_mean_site_90_centile_rural_pm25.png')
plt.show() 
    
for i_day in range(n_days):
    x = date[i_day]
    #print x
    for i_site in range(n_gd_sites): 
        y = stats_sites[3,i_site]
        #print y
        plt.scatter(x,y)
plt.xlim(date.min(), date.max())
plt.ylim(0, 100)
plt.xlabel('Year')
plt.ylabel('PM$_{2.5}$ concentration')
plt.title('Mean Site 95th centile Rural PM$_{2.5}$ Concentration 2010-2016')
plt.savefig('gdsites_mean_site_95_centile_rural_pm25.png')
plt.show() 

## PLOT OF DAYS ##

for i_day in range(n_days): 
    x = date[i_day]
    y = stats_days[3,i_day]
    #print y
    plt.scatter(x,y)
plt.xlim(date.min(), date.max())
plt.ylim(0, 100)
plt.xlabel('Year')
plt.ylabel('PM$_{2.5}$ concentration')
plt.title('Mean Daily 95th centile Rural PM$_{2.5}$ Concentration 2010-2016')
plt.savefig('gdsites_mean_daily_95_centile_rural_pm25.png')
plt.show() 
    


