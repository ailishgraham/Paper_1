#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:24:31 2018

@author: ee15amg
"""

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
from datetime import datetime
import math


df = pd.read_csv("/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/pm25_rural_data/pm25.csv",parse_dates=[0],usecols=[0,9,10,11,12,13,14,15,16,17,18,19,20,
                                         21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52])

#Replace Date String with Datetime
df = df.replace('No data', np.NaN)
df['Date'] = pd.to_datetime(df['Date'])
#print 'datetype', type(date)
#print df['Date'], type(df['Date']),np.shape(df['Date']), len(df['Date'])
df = df.set_index(['Date'])

n_months_all = (12*7)
n_sites = (len(df.columns))


good_qual_data = np.zeros([n_sites,n_months_all])
## CHange years here ####


data_month = ['jan2010', 'feb2010', 'mar2010', 'apr2010', 'may2010', 'jun2010', 
              'jul2010', 'aug2010', 'sept2010', 'oct2010', 'nov2010', 'dec2010']
month_start_look_up = ['2010-01-01', '2010-02-01', '2010-03-01', '2010-04-01',
                       '2010-05-01', '2010-06-01', '2010-07-01', '2010-08-01',
                       '2010-09-01', '2010-10-01', '2010-11-01', '2010-12-01']
month_end_look_up = ['2010-01-31', '2010-02-28', '2010-03-31', '2010-04-30',
                       '2010-05-31', '2010-06-30', '2010-07-31', '2010-08-31',
                       '2010-09-30', '2010-10-31', '2010-11-30', '2010-12-31']
month_length = ['31','28','31','30','31','30','31','31','30','31','30','31']
n_days = (31)
n_sites = (len(df.columns))
n_months = (len(data_month))
#print 'sites, days, months', n_sites,n_days,n_months
data_monthly_2010 = np.zeros([n_months, n_sites, n_days])     

for i_month in range(len(data_month)):
    #print 'IMONTH', i_month
    #print 'len_month', month_length[i_month]
    n_days_month = month_length[i_month]
    #time.sleep(10)
    #print 'dates selected', data_year[i_year], date_start_look_up[i_year], date_end_look_up[i_year]
    data_month[i_month] = (df.loc[month_start_look_up[i_month]:month_end_look_up[i_month]])
    #print 'len_data', len(data_month[i_month])
 
    for i_day in range(len(data_month[i_month])):
        for i_site in range(n_sites):
            #print 'day,site', i_day,  i_site
            temp_data = data_month[i_month].iloc[i_day,i_site]
            data_monthly_2010[i_month,i_site,i_day] = float(temp_data)
    #print data_monthly[i_month,i_site,i_day]
    #print 'np.shape', np.shape(data_monthly)
    
    ## calculate data quality for each site ##
    good_sites_2010 = []    
    for i_site in range(n_sites):
        #print 'site, month', i_site, i_month
        temp_centile_data_flattened = np.ndarray.flatten(data_monthly_2010[i_month,i_site,:])
        #print 'temp_array', temp_centile_data_flattened
        sorted_array = np.sort(temp_centile_data_flattened)
        #print np.size(sorted_array)
        data_qual = (float(np.isnan(sorted_array).sum())/float(np.size(sorted_array))*100)
        #print 'imonth', i_month, 'isite', i_site, 'dq',data_qual

    ## If data availability >85% add to list of good sites ##
        
        if data_qual < 10: 
            #print 'good dq',i_site
            #print 'month, site', i_month, i_site
            good_sites_2010.append(i_site)
    print 'i_month,good_sites_2010',i_month, good_sites_2010
time.sleep(5)


data_month = ['jan2011', 'feb2011', 'mar2011', 'apr2011', 'may2011', 'jun2011', 
              'jul2011', 'aug2011', 'sept2011', 'oct2011', 'nov2011', 'dec2011']
month_start_look_up = ['2011-01-01', '2011-02-01', '2011-03-01', '2011-04-01',
                       '2011-05-01', '2011-06-01', '2011-07-01', '2011-08-01',
                       '2011-09-01', '2011-10-01', '2011-11-01', '2011-12-01']
month_end_look_up = ['2011-01-31', '2011-02-28', '2011-03-31', '2011-04-30',
                       '2011-05-31', '2011-06-30', '2011-07-31', '2011-08-31',
                       '2011-09-30', '2011-10-31', '2011-11-30', '2011-12-31']
month_length = ['31','28','31','30','31','30','31','31','30','31','30','31']
n_days = (31)
n_sites = (len(df.columns))
n_months = (len(data_month))
#print 'sites, days, months', n_sites,n_days,n_months
data_monthly_2011 = np.zeros([n_months, n_sites, n_days])     

for i_month in range(len(data_month)):
    #print 'IMONTH', i_month
    #print 'len_month', month_length[i_month]
    n_days_month = month_length[i_month]
    #time.sleep(10)
    #print 'dates selected', data_year[i_year], date_start_look_up[i_year], date_end_look_up[i_year]
    data_month[i_month] = (df.loc[month_start_look_up[i_month]:month_end_look_up[i_month]])
    #print 'len_data', len(data_month[i_month])
 
    for i_day in range(len(data_month[i_month])):
        for i_site in range(n_sites):
            #print 'day,site', i_day,  i_site
            temp_data = data_month[i_month].iloc[i_day,i_site]
            data_monthly_2011[i_month,i_site,i_day] = float(temp_data)
    #print data_monthly[i_month,i_site,i_day]
    #print 'np.shape', np.shape(data_monthly)
    
    ## calculate data quality for each site ##
    good_sites_2011 = []    
    for i_site in range(n_sites):
        #print 'site, month', i_site, i_month
        temp_centile_data_flattened = np.ndarray.flatten(data_monthly_2011[i_month,i_site,:])
        #print 'temp_array', temp_centile_data_flattened
        sorted_array = np.sort(temp_centile_data_flattened)
        #print np.size(sorted_array)
        data_qual = (float(np.isnan(sorted_array).sum())/float(np.size(sorted_array))*100)
        #print 'imonth', i_month, 'isite', i_site, 'dq',data_qual

    ## If data availability >85% add to list of good sites ##
        
        if data_qual < 10: 
            #print 'good dq',i_site
            #print 'month, site', i_month, i_site
            good_sites_2011.append(i_site)
    print 'i_month,good_sites_2011',i_month, good_sites_2011
time.sleep(5)



data_month = ['jan2012', 'feb2012', 'mar2012', 'apr2012', 'may2012', 'jun2012', 
              'jul2012', 'aug2012', 'sept2012', 'oct2012', 'nov2012', 'dec2012']
month_start_look_up = ['2012-01-01', '2012-02-01', '2012-03-01', '2012-04-01',
                       '2012-05-01', '2012-06-01', '2012-07-01', '2012-08-01',
                       '2012-09-01', '2012-10-01', '2012-11-01', '2012-12-01']
month_end_look_up = ['2012-01-31', '2012-02-28', '2012-03-31', '2012-04-30',
                       '2012-05-31', '2012-06-30', '2012-07-31', '2012-08-31',
                       '2012-09-30', '2012-10-31', '2012-11-30', '2012-12-31']
month_length = ['31','29','31','30','31','30','31','31','30','31','30','31']
n_days = (31)
n_sites = (len(df.columns))
n_months = (len(data_month))
#print 'sites, days, months', n_sites,n_days,n_months
data_monthly_2012 = np.zeros([n_months, n_sites, n_days])     

for i_month in range(len(data_month)):
    #print 'IMONTH', i_month
    #print 'len_month', month_length[i_month]
    n_days_month = month_length[i_month]
    #time.sleep(10)
    #print 'dates selected_2012', month_start_look_up[i_month], month_end_look_up[i_month]
    data_month[i_month] = (df.loc[month_start_look_up[i_month]:month_end_look_up[i_month]])
    #print 'len_data', len(data_month[i_month])
 
    for i_day in range(len(data_month[i_month])):
        for i_site in range(n_sites):
            #print 'day,site', i_day,  i_site
            temp_data = data_month[i_month].iloc[i_day,i_site]
            data_monthly_2012[i_month,i_site,i_day] = float(temp_data)
    #print data_monthly[i_month,i_site,i_day]
    #print 'np.shape', np.shape(data_monthly)
    
    ## calculate data quality for each site ##
    
    good_sites_2012 = []
    
    for i_site in range(n_sites):
        #print 'site, month', i_site, i_month
        temp_centile_data_flattened = np.ndarray.flatten(data_monthly_2012[i_month,i_site,:])
        #print 'temp_array', temp_centile_data_flattened
        sorted_array = np.sort(temp_centile_data_flattened)
        #print np.size(sorted_array)
        data_qual = (float(np.isnan(sorted_array).sum())/float(np.size(sorted_array))*100)
        #print 'imonth', i_month, 'isite', i_site, 'dq',data_qual
        time.sleep(1)
    ## If data availability >85% add to list of good sites ##
        
    
        if data_qual < 10: 
            #print 'good dq',i_site
            #print 'month, site', i_month, i_site
            good_sites_2012.append(i_site)
    print 'i_month,good_sites_2012',i_month, good_sites_2012
time.sleep(5)




data_month = ['jan2013', 'feb2013', 'mar2013', 'apr2013', 'may2013', 'jun2013', 
              'jul2013', 'aug2013', 'sept2013', 'oct2013', 'nov2013', 'dec2013']
month_start_look_up = ['2013-01-01', '2013-02-01', '2013-03-01', '2013-04-01',
                       '2013-05-01', '2013-06-01', '2013-07-01', '2013-08-01',
                       '2013-09-01', '2013-10-01', '2013-11-01', '2013-12-01']
month_end_look_up = ['2013-01-31', '2013-02-28', '2013-03-31', '2013-04-30',
                       '2013-05-31', '2013-06-30', '2013-07-31', '2013-08-31',
                       '2013-09-30', '2013-10-31', '2013-11-30', '2013-12-31']
month_length = ['31','28','31','30','31','30','31','31','30','31','30','31']
n_days = (31)
n_sites = (len(df.columns))
n_months = (len(data_month))
#print 'sites, days, months', n_sites,n_days,n_months
data_monthly_2013 = np.zeros([n_months, n_sites, n_days])     

for i_month in range(len(data_month)):
    #print 'IMONTH', i_month
    #print 'len_month', month_length[i_month]
    n_days_month = month_length[i_month]
    #time.sleep(10)
    #print 'dates selected_2013', month_start_look_up[i_month], month_end_look_up[i_month]
    data_month[i_month] = (df.loc[month_start_look_up[i_month]:month_end_look_up[i_month]])
    #print 'len_data', len(data_month[i_month])
 
    for i_day in range(len(data_month[i_month])):
        for i_site in range(n_sites):
            #print 'day,site', i_day,  i_site
            temp_data = data_month[i_month].iloc[i_day,i_site]
            data_monthly_2013[i_month,i_site,i_day] = float(temp_data)
    #print data_monthly[i_month,i_site,i_day]
    #print 'np.shape', np.shape(data_monthly)
    
    ## calculate data quality for each site ##
    
    
    good_sites_2013 = []   
    for i_site in range(n_sites):
        #print 'site, month', i_site, i_month
        temp_centile_data_flattened = np.ndarray.flatten(data_monthly_2013[i_month,i_site,:])
        #print 'temp_array', temp_centile_data_flattened
        sorted_array = np.sort(temp_centile_data_flattened)
        #print np.size(sorted_array)
        data_qual = (float(np.isnan(sorted_array).sum())/float(np.size(sorted_array))*100)
        #print 'imonth', i_month, 'isite', i_site, 'dq',data_qual
    ## If data availability >85% add to list of good sites ##
        

        if data_qual < 10: 
            #print 'good dq',i_site
            #print 'month, site', i_month, i_site
            good_sites_2013.append(i_site)
    print 'i_month,good_sites_2013',i_month, good_sites_2013
time.sleep(5)




data_month = ['jan2014', 'feb2014', 'mar2014', 'apr2014', 'may2014', 'jun2014', 
              'jul2014', 'aug2014', 'sept2014', 'oct2014', 'nov2014', 'dec2014']
month_start_look_up = ['2014-01-01', '2014-02-01', '2014-03-01', '2014-04-01',
                       '2014-05-01', '2014-06-01', '2014-07-01', '2014-08-01',
                       '2014-09-01', '2014-10-01', '2014-11-01', '2014-12-01']
month_end_look_up = ['2014-01-31', '2014-02-28', '2014-03-31', '2014-04-30',
                       '2014-05-31', '2014-06-30', '2014-07-31', '2014-08-31',
                       '2014-09-30', '2014-10-31', '2014-11-30', '2014-12-31']
month_length = ['31','28','31','30','31','30','31','31','30','31','30','31']
n_days = (31)
n_sites = (len(df.columns))
n_months = (len(data_month))
#print 'sites, days, months', n_sites,n_days,n_months
data_monthly_2014 = np.zeros([n_months, n_sites, n_days])     

for i_month in range(len(data_month)):
    #print 'IMONTH', i_month
    #print 'len_month', month_length[i_month]
    n_days_month = month_length[i_month]
    #time.sleep(10)
    #print 'dates selected', data_year[i_year], date_start_look_up[i_year], date_end_look_up[i_year]
    data_month[i_month] = (df.loc[month_start_look_up[i_month]:month_end_look_up[i_month]])
    #print 'len_data', len(data_month[i_month])
 
    for i_day in range(len(data_month[i_month])):
        for i_site in range(n_sites):
            #print 'day,site', i_day,  i_site
            temp_data = data_month[i_month].iloc[i_day,i_site]
            data_monthly_2014[i_month,i_site,i_day] = float(temp_data)
    #print data_monthly[i_month,i_site,i_day]
    #print 'np.shape', np.shape(data_monthly)
    
    ## calculate data quality for each site ##
    good_sites_2014 = []
    for i_site in range(n_sites):
        #print 'site, month', i_site, i_month
        temp_centile_data_flattened = np.ndarray.flatten(data_monthly_2014[i_month,i_site,:])
        #print 'temp_array_2014', temp_centile_data_flattened
        time.sleep(5)
        sorted_array = np.sort(temp_centile_data_flattened)
        #print np.size(sorted_array)
        data_qual = (float(np.isnan(sorted_array).sum())/float(np.size(sorted_array))*100)
        #print 'imonth', i_month, 'isite', i_site, 'dq',data_qual

    ## If data availability >85% add to list of good sites ##
        
        
        if data_qual < 10: 
            #print 'good dq',i_site
            #print 'month, site', i_month, i_site
            good_sites_2014.append(i_site)
    print 'i_month,good_sites_2014',i_month, good_sites_2014
time.sleep(5)



data_month = ['jan2015', 'feb2015', 'mar2015', 'apr2015', 'may2015', 'jun2015', 
              'jul2015', 'aug2015', 'sept2015', 'oct2015', 'nov2015', 'dec2015']
month_start_look_up = ['2015-01-01', '2015-02-01', '2015-03-01', '2015-04-01',
                       '2015-05-01', '2015-06-01', '2015-07-01', '2015-08-01',
                       '2015-09-01', '2015-10-01', '2015-11-01', '2015-12-01']
month_end_look_up = ['2015-01-31', '2015-02-28', '2015-03-31', '2015-04-30',
                       '2015-05-31', '2015-06-30', '2015-07-31', '2015-08-31',
                       '2015-09-30', '2015-10-31', '2015-11-30', '2015-12-31']
month_length = ['31','28','31','30','31','30','31','31','30','31','30','31']
n_days = (31)
n_sites = (len(df.columns))
n_months = (len(data_month))
#print 'sites, days, months', n_sites,n_days,n_months
data_monthly_2015 = np.zeros([n_months, n_sites, n_days])     

for i_month in range(len(data_month)):
    #print 'IMONTH', i_month
    #print 'len_month', month_length[i_month]
    n_days_month = month_length[i_month]
    #time.sleep(10)
    #print 'dates selected', data_year[i_year], date_start_look_up[i_year], date_end_look_up[i_year]
    data_month[i_month] = (df.loc[month_start_look_up[i_month]:month_end_look_up[i_month]])
    #print 'len_data', len(data_month[i_month])
 
    for i_day in range(len(data_month[i_month])):
        for i_site in range(n_sites):
            #print 'day,site', i_day,  i_site
            temp_data = data_month[i_month].iloc[i_day,i_site]
            data_monthly_2015[i_month,i_site,i_day] = float(temp_data)
    #print data_monthly[i_month,i_site,i_day]
    #print 'np.shape', np.shape(data_monthly)
    
    ## calculate data quality for each site ##
    good_sites_2015 = []   
    for i_site in range(n_sites):
        #print 'site, month', i_site, i_month
        temp_centile_data_flattened = np.ndarray.flatten(data_monthly_2015[i_month,i_site,:])
        #print 'temp_array', temp_centile_data_flattened
        sorted_array = np.sort(temp_centile_data_flattened)
        #print np.size(sorted_array)
        data_qual = (float(np.isnan(sorted_array).sum())/float(np.size(sorted_array))*100)
        #print 'imonth', i_month, 'isite', i_site, 'dq',data_qual

    ## If data availability >85% add to list of good sites ##
        

        if data_qual < 10: 
            #print 'good dq',i_site
            #print 'month, site', i_month, i_site
            good_sites_2015.append(i_site)
    print 'i_month,good_sites_2015',i_month, good_sites_2015
time.sleep(5)




data_month = ['jan2016', 'feb2016', 'mar2016', 'apr2016', 'may2016', 'jun2016', 
              'jul2016', 'aug2016', 'sept2016', 'oct2016', 'nov2016', 'dec2016']
month_start_look_up = ['2016-01-01', '2016-02-01', '2016-03-01', '2016-04-01',
                       '2016-05-01', '2016-06-01', '2016-07-01', '2016-08-01',
                       '2016-09-01', '2016-10-01', '2016-11-01', '2016-12-01']
month_end_look_up = ['2016-01-31', '2016-02-28', '2016-03-31', '2016-04-30',
                       '2016-05-31', '2016-06-30', '2016-07-31', '2016-08-31',
                       '2016-09-30', '2016-10-31', '2016-11-30', '2016-12-31']
month_length = ['31','29','31','30','31','30','31','31','30','31','30','31']
n_days = (31)
n_sites = (len(df.columns))
n_months = (len(data_month))
#print 'sites, days, months', n_sites,n_days,n_months
data_monthly_2016 = np.zeros([n_months, n_sites, n_days])     

for i_month in range(len(data_month)):
    #print 'IMONTH', i_month
    #print 'len_month', month_length[i_month]
    n_days_month = month_length[i_month]
    #time.sleep(10)
    #print 'dates selected', data_year[i_year], date_start_look_up[i_year], date_end_look_up[i_year]
    data_month[i_month] = (df.loc[month_start_look_up[i_month]:month_end_look_up[i_month]])
    #print 'len_data', len(data_month[i_month])
 
    for i_day in range(len(data_month[i_month])):
        for i_site in range(n_sites):
            #print 'day,site', i_day,  i_site
            temp_data = data_month[i_month].iloc[i_day,i_site]
            data_monthly_2016[i_month,i_site,i_day] = float(temp_data)
    #print data_monthly[i_month,i_site,i_day]
    #print 'np.shape', np.shape(data_monthly)
    
    ## calculate data quality for each site ##
    good_sites_2016 = []    
    for i_site in range(n_sites):
        #print 'site, month', i_site, i_month
        temp_centile_data_flattened = np.ndarray.flatten(data_monthly_2016[i_month,i_site,:])
        #print 'temp_array', temp_centile_data_flattened
        sorted_array = np.sort(temp_centile_data_flattened)
        #print np.size(sorted_array)
        data_qual = (float(np.isnan(sorted_array).sum())/float(np.size(sorted_array))*100)
        #print 'imonth', i_month, 'isite', i_site, 'dq',data_qual

    ## If data availability >85% add to list of good sites ##
        

        if data_qual < 10: 
            #print 'good dq',i_site
            #print 'month, site', i_month, i_site
            good_sites_2016.append(i_site)
    print 'i_month,good_sites_2016',i_month, good_sites_2016
time.sleep(5)


## PLOT OF DAYS ##

for isite in len(range(good_sites_2010)): 
    x = data_month[i_month]
    print x
    y = good_sites_2010[isite]
    print y
    plt.scatter(x,y)
plt.xlim(data_month[0], len(data_month))
plt.ylim(0, 43)
plt.xlabel('Year')
plt.ylabel('Site')
plt.title('Data Quality')
#plt.savefig('gdsites_mean_daily_95_centile_rural_pm25.png')
plt.show() 
    

#%%
#############################
#############################
#############################








######## Create arrays and Read in data ###########

##################
# 1st array n_days by n_sites
##################

#n_sites = (len(df.columns))
##print n_sites
#n_days = (len(df.index))
##print i_days
#date_info = np.zeros([n_days])
##print 'day.shape',cluster_data_day.shape
#
#for i_day in range(n_days):
#    temp_data = time_data.iloc[i_day]
##    date = datetime.strptime(date[i_day], '%Y-%m-%d')
#    print temp_data, type(temp_data)
#    date_info[i_day] = date



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





    

#%%
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
#plt.savefig('gdsites_mean_site_90_centile_rural_pm25.png')
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
#plt.savefig('gdsites_mean_site_95_centile_rural_pm25.png')
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
#plt.savefig('gdsites_mean_daily_95_centile_rural_pm25.png')
plt.show() 
    


