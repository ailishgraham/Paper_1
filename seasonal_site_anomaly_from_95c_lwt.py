#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:24:03 2018

@author: ee15amg
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 08:38:49 2018

@author: ee15amg
"""


from mpl_toolkits.basemap import Basemap
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
from scipy import stats


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 09:18:01 2018

@author: ee15amg
"""

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

from mpl_toolkits.basemap import Basemap
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

df = pd.read_csv("/nfs/a201/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/pm25_rural_data/pm25.csv",parse_dates=[0],usecols=[0,9,10,11,12,13,14,15,16,17,18,19,20,
                                         21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52])
df_lwt = pd.read_csv("/nfs/a201/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/pm25_rural_data/pm25.csv",usecols=[0,8])
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


lons = [-2.094278,	-3.2429, -5.928833, -1.829999, -3.007175, -2.584482, -3.17625,
        -1.454946, -1.438228, -1.560228, -7.331179, 0.271611, -3.182186, -4.243631,
        -0.341222, -1.533119, -1.546472, -1.127311, 0.184806, -0.125889, 0.070766,
        -0.298777,	-0.213492,-0.345606, -2.237881, -1.610528, -2.977281, 1.301976, 
        -1.146447, -1.260278, -4.142361, -1.068583, -2.680353, -0.944067, 0.634889,
        -2.334139, -1.478096, -1.395778,	0.678408, -2.175133, -1.406878,	-2.638139, 
        -3.022722, -1.086514]

lats = [57.15736, 55.79216, 54.59965, 52.437165, 53.80489, 51.462839, 51.48178,
        53.244131, 51.149617, 52.411563, 55.002818	, 50.805778, 55.945589, 55.865782,
        53.74878, 52.28881, 53.80378, 52.619823, 51.46603, 51.52229, 51.45258,
        51.617333, 51.52105, 51.425286, 53.48152, 54.97825, 51.601203, 52.614193,
        52.95473, 51.744806, 50.37167, 50.82881, 53.76559, 51.45309, 51.456170,
        53.48481, 53.378622	, 50.90814, 51.544206, 53.02821, 54.88361	, 53.54914, 
        53.37287, 53.967513]

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
print ('shape data', np.shape(data_monthly_checked), np.shape(data_monthly_lwt))
print ('data', data_monthly_checked[:,:,:])
print ('lwt', data_monthly_lwt[:,:])

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
all_data = np.empty([n_months,n_sites,n_days])
all_data[:,:,:] = np.nan



## Loop through lwt array to select each lwt for all sites for each year

NE_index = [1,11,21]
E_index = [2,12,22]
SE_index = [3,13,23]
S_index = [4,14,24]
SW_index = [5,15,25]
W_index = [6,16,26]
NW_index = [7,17,27]
N_index = [8,18,28]
all_index = [1,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28]


## Create arrays for lwt data combined and statistics/boxplots


## SPRING 


lamb_weather_type = ['N','NE','E','SE','S','SW','W','NW','all']
n_lwt = len(lamb_weather_type)
lwt_array_monthly = np.empty([n_lwt,n_months,n_sites,n_days])
lwt_array_monthly[:,:,:,:] = np.nan
n_stats = 5
n_seasons = 4
statistics_seasonal = np.zeros([n_stats,n_seasons,n_lwt,n_sites])
lwt_anomaly_seasonal = np.zeros([n_stats,n_seasons,n_lwt,n_sites])


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


    
    #Look for all flow types
    all_flow = np.where((data_monthly_lwt[i_month,:] == all_index[0]) | (data_monthly_lwt[i_month,:] == all_index[1]) 
    | (data_monthly_lwt[i_month,:] == all_index[2]) | (data_monthly_lwt[i_month,:] == all_index[3])
    | (data_monthly_lwt[i_month,:] == all_index[4]) | (data_monthly_lwt[i_month,:] == all_index[5]) 
    | (data_monthly_lwt[i_month,:] == all_index[6]) | (data_monthly_lwt[i_month,:] == all_index[7])
    | (data_monthly_lwt[i_month,:] == all_index[8]) | (data_monthly_lwt[i_month,:] == all_index[9])
    | (data_monthly_lwt[i_month,:] == all_index[10]) | (data_monthly_lwt[i_month,:] == all_index[11]) 
    | (data_monthly_lwt[i_month,:] == all_index[12]) | (data_monthly_lwt[i_month,:] == all_index[13])
    | (data_monthly_lwt[i_month,:] == all_index[14]) | (data_monthly_lwt[i_month,:] == all_index[15])
    | (data_monthly_lwt[i_month,:] == all_index[16]) | (data_monthly_lwt[i_month,:] == all_index[17]) 
    | (data_monthly_lwt[i_month,:] == all_index[18]) | (data_monthly_lwt[i_month,:] == all_index[19])
    | (data_monthly_lwt[i_month,:] == all_index[20]) | (data_monthly_lwt[i_month,:] == all_index[21])
    | (data_monthly_lwt[i_month,:] == all_index[22]) | (data_monthly_lwt[i_month,:] == all_index[23]))
   
    

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
        temp_data_all = data_monthly_checked[i_month,i_site,all_flow]
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
        all_data[i_month,i_site,all_flow] = temp_data_all
    #print 'N_data', NE_data[0,0,:]
#print 'NE_data', SE_data[:,:,:]


## Fill lwt_array with data for pm25 concs in each lwt 
        
lwt_array_monthly[0,:,:,:] = N_data[:,:,:]
lwt_array_monthly[1,:,:,:] = NE_data[:,:,:]
lwt_array_monthly[2,:,:,:] = E_data[:,:,:]
lwt_array_monthly[3,:,:,:] = SE_data[:,:,:]
lwt_array_monthly[4,:,:,:] = S_data[:,:,:]
lwt_array_monthly[5,:,:,:] = SW_data[:,:,:]
lwt_array_monthly[6,:,:,:] = W_data[:,:,:]
lwt_array_monthly[7,:,:,:] = NW_data[:,:,:]
lwt_array_monthly[8,:,:,:] = all_data[:,:,:]

#print 'lwt0', lwt_array[0,:,:,:]
#print 'lwt7', lwt_array[7,0:3,:,:]
#np.save('lwt_monthly_anomaly', lwt_array_monthly,allow_pickle=True, fix_imports=True)


print ('SPRING')
for i_lwt in range(len(lamb_weather_type)):
    for i_site in range(n_sites):
        start = 2
        stop = 5
        d_flattened = []
        #print 'list', d_flattened
        while start < 75:
           # for i_month in range(n_months):
            #print 'lwt = ', i_lwt, 'start', start, 'stop', stop
            flattened_array= np.ndarray.flatten(lwt_array_monthly[i_lwt,start:stop, i_site, :])
            d_flattened.append(flattened_array)
            #print d_flattened, len(d_flattened)
            #time.sleep(3)
            #print len(d_flattened), d_flattened
            ##time.sleep(3)
            start = start + 12
            stop = stop + 12
        #print 'lwt', lamb_weather_type[i_lwt]
        #print 'non-nan', np.count_nonzero(~np.isnan(d_flattened))
        #print 'len_array', np.shape(d_flattened)
        centile50 = np.nanpercentile(d_flattened, 50)
        statistics_seasonal[0,0,i_lwt,i_site]= centile50
        #print '50=', centile50
        #time.sleep(2)
        centile25 = np.nanpercentile(d_flattened, 25)
        statistics_seasonal[1,0,i_lwt,i_site]= centile25
        #print '25=', centile25
        #time.sleep(2)
        centile75 = np.nanpercentile(d_flattened, 75)
        statistics_seasonal[2,0,i_lwt,i_site]= centile75
        #print '75=', centile75
        #time.sleep(2)
        centile90 = np.nanpercentile(d_flattened, 90)
        statistics_seasonal[3,0,i_lwt,i_site]= centile90
        #print '90=', centile90
        #time.sleep(2)
        centile10 = np.nanpercentile(d_flattened, 10)
        statistics_seasonal[4,0,i_lwt,i_site]= centile10
        #print '10=', centile10
        #time.sleep(2)
#time.sleep(500)
 
### SUMMER ##    
    

print ('SUMMER')
for i_lwt in range(len(lamb_weather_type)):
    for i_site in range(n_sites):
        start = 5
        stop = 8
        d_flattened_summer = []
        #print 'list', d_flattened_summer
        while start < 78:
           # for i_month in range(n_months):
            #print 'lwt = ', i_lwt, 'start', start, 'stop', stop
            flattened_array_summer= np.ndarray.flatten(lwt_array_monthly[i_lwt,start:stop, i_site, :])
            d_flattened_summer.append(flattened_array_summer)
            #print d_flattened, len(d_flattened)
            ##time.sleep(1)
            #print len(d_flattened), d_flattened
            ##time.sleep(3)
            start = start + 12
            stop = stop + 12
        #print 'lwt', lamb_weather_type[i_lwt]
        #print 'non-nan', np.count_nonzero(~np.isnan(d_flattened_summer))
        #print 'len_array', np.shape(d_flattened_summer)
        #time.sleep(10)
        centile50 = np.nanpercentile(d_flattened_summer, 50)
        statistics_seasonal[0,1,i_lwt,i_site]= centile50
        #print '50=', centile50
        ##time.sleep(2)
        centile25 = np.nanpercentile(d_flattened_summer, 25)
        statistics_seasonal[1,1,i_lwt,i_site]= centile25
        #print '25=', centile25
        ##time.sleep(2)
        centile75 = np.nanpercentile(d_flattened_summer, 75)
        statistics_seasonal[2,1,i_lwt,i_site]= centile75
        #print '75=', centile75
        ##time.sleep(2)
        centile90 = np.nanpercentile(d_flattened_summer, 90)
        statistics_seasonal[3,1,i_lwt,i_site]= centile90
        #print '90=', centile90
        ##time.sleep(2)
        centile10 = np.nanpercentile(d_flattened_summer, 10)
        statistics_seasonal[4,1,i_lwt,i_site]= centile10
        #print '10=', centile10
        ##time.sleep(5)
        #time.sleep(10)
        
    
## AUTUMN 
print ('AUTUMN')
for i_lwt in range(len(lamb_weather_type)):
    for i_site in range(n_sites):
        start = 8
        stop = 11
        d_flattened_autumn = []
        #print 'list', d_flattened_autumn
        while start < 80:
           # for i_month in range(n_months):
            #print 'lwt = ', i_lwt, 'start', start, 'stop', stop
            flattened_array_autumn= np.ndarray.flatten(lwt_array_monthly[i_lwt,start:stop, i_site, :])
            d_flattened_autumn.append(flattened_array_autumn)
            #print d_flattened, len(d_flattened)
            ##time.sleep(1)
            #print len(d_flattened), d_flattened
            ##time.sleep(3)
            start = start + 12
            stop = stop + 12
        #print 'lwt', lamb_weather_type[i_lwt]
        #print 'non-nan', np.count_nonzero(~np.isnan(d_flattened_autumn))
        ##print 'len_array', np.shape(d_flattened_autumn)
        #time.sleep(10)
        centile50 = np.nanpercentile(d_flattened_autumn, 50)
        statistics_seasonal[0,2,i_lwt,i_site]= centile50
        #print '50=', centile50
        ##time.sleep(2)
        centile25 = np.nanpercentile(d_flattened_autumn, 25)
        statistics_seasonal[1,2,i_lwt,i_site]= centile25
        #print '25=', centile25
        ##time.sleep(2)
        centile75 = np.nanpercentile(d_flattened_autumn, 75)
        statistics_seasonal[2,2,i_lwt,i_site]= centile75
        #print '75=', centile75
        ##time.sleep(2)
        centile90 = np.nanpercentile(d_flattened_autumn, 90)
        statistics_seasonal[3,2,i_lwt,i_site]= centile90
        #print '90=', centile90
        ##time.sleep(2)
        centile10 = np.nanpercentile(d_flattened_autumn, 10)
        statistics_seasonal[4,2,i_lwt,i_site]= centile10
        #print '10=', centile10
        ##time.sleep(5)
        #time.sleep(10)
    
  
    ## WINTER

print ('WINTER' )
for i_lwt in range(len(lamb_weather_type)):
    for i_site in range(n_sites):
        start = 11
        stop = 14
        d_flattened_winter = []
        #print 'list', d_flattened_winter
        while start < 83:
           # for i_month in range(n_months):
            #print 'lwt = ', i_lwt, 'start', start, 'stop', stop
            if start == 83:
                flattened_array_winter= np.ndarray.flatten(lwt_array_monthly[i_lwt,start:84, :, :])  
            else:
                flattened_array_winter= np.ndarray.flatten(lwt_array_monthly[i_lwt,start:stop, i_site, :])
                d_flattened_winter.append(flattened_array_winter)
                #print d_flattened, len(d_flattened)
                ##time.sleep(1)
                #print len(d_flattened), d_flattened
                ##time.sleep(3)
                start = start + 12
                stop = stop + 12
        #print 'lwt', lamb_weather_type[i_lwt]
        #print 'non-nan', np.count_nonzero(~np.isnan(d_flattened_winter))
        #print 'len_array', np.shape(d_flattened_winter)
        #time.sleep(2)
        centile50 = np.nanpercentile(d_flattened_winter, 50)
        statistics_seasonal[0,3,i_lwt,i_site]= centile50
        #print '50=', centile50
        ##time.sleep(2)
        centile25 = np.nanpercentile(d_flattened_winter, 25)
        statistics_seasonal[1,3,i_lwt,i_site]= centile25
        #print '25=', centile25
        ##time.sleep(2)
        centile75 = np.nanpercentile(d_flattened_winter, 75)
        statistics_seasonal[2,3,i_lwt,i_site]= centile75
        #print '75=', centile75
        ##time.sleep(2)
        centile90 = np.nanpercentile(d_flattened_winter, 90)
        statistics_seasonal[3,3,i_lwt,i_site]= centile90
        #print '90=', centile90
        ##time.sleep(2)
        centile10 = np.nanpercentile(d_flattened_winter, 10)
        statistics_seasonal[4,3,i_lwt,i_site]= centile10
        #print '10=', centile10
        ##time.sleep(5)
        #time.sleep(10)


##Calculate anomalies in each stat value for each season at each site
for i_stat in range(n_stats):    
    for i_season in range(n_seasons):
        for i_lwt in range(len(lamb_weather_type)-1):
            for i_site in range(n_sites):
                #print('stat',i_stat,'seas',i_season,'lwt',i_lwt,'site',i_site)
                temp_data_anom = ((statistics_seasonal[i_stat,i_season,i_lwt,i_site])-(statistics_seasonal[i_stat,i_season,8,i_site]))
                #time.sleep(2)
                #print('td=',temp_data_anom)
                #time.sleep(5)
                lwt_anomaly_seasonal[i_stat,i_season,i_lwt,i_site]=temp_data_anom
#print('stat lwt',statistics[3,0,0,0],'stat lwt all',statistics[3,0,3,0], 'anom',lwt_anomaly[3,0,0,0])
#print(lwt_anomaly_seasonal[3,0,3,0])   
 
               
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
##Create map 
for i_season in range(n_seasons):                              
    fig = plt.figure(figsize=(16, 20))
    for i_lwt in range(len(lamb_weather_type)-1):
        ax = fig.add_subplot(2, 4, i_lwt+1)  
        map = Basemap(projection='merc', lat_0 = 57, lon_0 = -4,
                              resolution = 'i', area_thresh = 0.05,
                              llcrnrlon=-12, llcrnrlat=49,
                              urcrnrlon=4, urcrnrlat=61)
        map.drawcoastlines(linewidth = 1, zorder = 0)
        cmap = plt.cm.seismic
        # extract all colors from the .jet map
        cmaplist = [cmap(i) for i in range(cmap.N)]
        # create the new map
        cmap = cmap.from_list('Custom cmap', cmaplist, cmap.N)
        # define the bins and normalize
        bounds = np.linspace(-15,15,31)
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    
        data = lwt_anomaly_seasonal[3,i_season,i_lwt,:]
        #print('data = ', data)
        #time.sleep(2)
        xi,yi = map(lons,lats)
        #print 'lon, lat',  xi, yi
        print( 'creating plot',seasons[i_season],i_lwt)
        sc = map.scatter(xi,yi,s=50,c=data,vmin=-40,vmax=40,cmap=cmap)#,cmap=plt.cm.jet)#marker='o',color='k')
        ax.annotate(str(lamb_weather_type[i_lwt]), xy=(0.8, 0.8), xycoords="axes fraction",fontsize=15, fontweight='bold')
        fig.tight_layout()
    
    ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.02])
    cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, spacing='proportional', ticks=bounds, boundaries=bounds, format='%1i', orientation='horizontal')
    font_size = 15 # Adjust as appropriate.
    cb.ax.tick_params(labelsize=font_size)
    cb.set_label('Anomaly', fontsize=15)
    plt.savefig(str(seasons[i_season])+'_90th_percentile_anomalies.png')
    plt.show() 

##Create map 
for i_season in range(n_seasons):                              
    fig = plt.figure(figsize=(16, 20))
    for i_lwt in range(len(lamb_weather_type)-1):
        ax = fig.add_subplot(2, 4, i_lwt+1)  
        map = Basemap(projection='merc', lat_0 = 57, lon_0 = -4,
                              resolution = 'i', area_thresh = 0.05,
                              llcrnrlon=-12, llcrnrlat=49,
                              urcrnrlon=4, urcrnrlat=61)
        map.drawcoastlines(linewidth = 1, zorder = 0)
        cmap = plt.cm.seismic
        # extract all colors from the .jet map
        cmaplist = [cmap(i) for i in range(cmap.N)]
        # create the new map
        cmap = cmap.from_list('Custom cmap', cmaplist, cmap.N)
        # define the bins and normalize
        bounds = np.linspace(-15,15,31)
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    
        data = lwt_anomaly_seasonal[2,i_season,i_lwt,:]
        #print('data = ', data)
        #time.sleep(2)
        xi,yi = map(lons,lats)
        #print 'lon, lat',  xi, yi
        print( 'creating plot',seasons[i_season],i_lwt)
        sc = map.scatter(xi,yi,s=50,c=data,vmin=-40,vmax=40,cmap=cmap)#,cmap=plt.cm.jet)#marker='o',color='k')
        ax.annotate(str(lamb_weather_type[i_lwt]), xy=(0.8, 0.8), xycoords="axes fraction",fontsize=15, fontweight='bold')
        fig.tight_layout()
    
    ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.02])
    cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, spacing='proportional', ticks=bounds, boundaries=bounds, format='%1i', orientation='horizontal')
    font_size = 15 # Adjust as appropriate.
    cb.ax.tick_params(labelsize=font_size)
    cb.set_label('Anomaly', fontsize=15)
    plt.savefig(str(seasons[i_season])+'_75th_percentile_anomalies.png')
    plt.show()             
    
##Create map 
for i_season in range(n_seasons):                              
    fig = plt.figure(figsize=(16, 20))
    for i_lwt in range(len(lamb_weather_type)-1):
        ax = fig.add_subplot(2, 4, i_lwt+1)  
        map = Basemap(projection='merc', lat_0 = 57, lon_0 = -4,
                              resolution = 'i', area_thresh = 0.05,
                              llcrnrlon=-12, llcrnrlat=49,
                              urcrnrlon=4, urcrnrlat=61)
        map.drawcoastlines(linewidth = 1, zorder = 0)
        cmap = plt.cm.seismic
        # extract all colors from the .jet map
        cmaplist = [cmap(i) for i in range(cmap.N)]
        # create the new map
        cmap = cmap.from_list('Custom cmap', cmaplist, cmap.N)
        # define the bins and normalize
        bounds = np.linspace(-15,15,31)
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    
        data = lwt_anomaly_seasonal[0,i_season,i_lwt,:]
        #print('data = ', data)
        #time.sleep(2)
        xi,yi = map(lons,lats)
        #print 'lon, lat',  xi, yi
        print( 'creating plot',seasons[i_season],i_lwt)
        sc = map.scatter(xi,yi,s=50,c=data,vmin=-40,vmax=40,cmap=cmap)#,cmap=plt.cm.jet)#marker='o',color='k')
        ax.annotate(str(lamb_weather_type[i_lwt]), xy=(0.8, 0.8), xycoords="axes fraction",fontsize=15, fontweight='bold')
        fig.tight_layout()
    
    ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.02])
    cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, spacing='proportional', ticks=bounds, boundaries=bounds, format='%1i', orientation='horizontal')
    font_size = 15 # Adjust as appropriate.
    cb.ax.tick_params(labelsize=font_size)
    cb.set_label('Anomaly', fontsize=15)
    plt.savefig(str(seasons[i_season])+'_mean_anomalies.png')
    plt.show() 

#Plot true values for percentiles to compare anomalies to 
#
#seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
###Create map 
#for i_season in range(n_seasons):                              
#    fig = plt.figure(figsize=(16, 20))
#    for i_lwt in range(len(lamb_weather_type)-1):
#        ax = fig.add_subplot(2, 4, i_lwt+1)  
#        map = Basemap(projection='merc', lat_0 = 57, lon_0 = -4,
#                              resolution = 'i', area_thresh = 0.05,
#                              llcrnrlon=-12, llcrnrlat=49,
#                              urcrnrlon=4, urcrnrlat=61)
#        map.drawcoastlines(linewidth = 1, zorder = 0)
#        cmap = plt.cm.jet
#        # extract all colors from the .jet map
#        cmaplist = [cmap(i) for i in range(cmap.N)]
#        # create the new map
#        cmap = cmap.from_list('Custom cmap', cmaplist, cmap.N)
#        # define the bins and normalize
#        bounds = np.linspace(0,70,14)
#        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
#    
#        data = statistics_seasonal[2,i_season,i_lwt,:]
#        #print('data = ', data)
#        #time.sleep(2)
#        xi,yi = map(lons,lats)
#        #print 'lon, lat',  xi, yi
#        print( 'creating plot',seasons[i_season],i_lwt)
#        sc = map.scatter(xi,yi,s=50,c=data,vmin=0,vmax=70,cmap=cmap)#,cmap=plt.cm.jet)#marker='o',color='k')
#        ax.annotate(str(lamb_weather_type[i_lwt]), xy=(0.8, 0.8), xycoords="axes fraction",fontsize=15, fontweight='bold')
#        fig.tight_layout()
#    
#    ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.02])
#    cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, spacing='proportional', ticks=bounds, boundaries=bounds, format='%1i', orientation='horizontal')
#    font_size = 15 # Adjust as appropriate.
#    cb.ax.tick_params(labelsize=font_size)
#    cb.set_label('Concentration ${\mu}m$gm${^3}$', fontsize=15)
#    plt.savefig(str(seasons[i_season])+'_75th_percentile_values.png')
#    plt.show() 
               
                



##%%           
#seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
###Create map 
#for i_season in range(n_seasons):
#    fig = plt.figure(figsize=(20, 20))
#    fig.subplots_adjust(hspace=0.05, wspace=0.05)
#    for i_lwt in range(len(lamb_weather_type)-1): 
#        ax = fig.add_subplot(2, 4, i_lwt+1)
#        map = Basemap(projection='merc', lat_0 = 57, lon_0 = -4,
#                      resolution = 'i', area_thresh = 0.05,
#                      llcrnrlon=-12, llcrnrlat=49,
#                      urcrnrlon=4, urcrnrlat=61)
#        map.drawcoastlines(linewidth = 1, zorder = 0)
#        cmap = plt.cm.seismic
#        # extract all colors from the .jet map
#        cmaplist = [cmap(i) for i in range(cmap.N)]
#        # create the new map
#        cmap = cmap.from_list('Custom cmap', cmaplist, cmap.N)
#        # define the bins and normalize
#        bounds = np.linspace(-15,15,31)
#        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
#        
#        data = lwt_anomaly_seasonal[3,i_season,i_lwt,:]
#        #print('data = ', data)
#        #time.sleep(2)
#        xi,yi = map(lons,lats)
#        #print 'lon, lat',  xi, yi
#        print( 'creating plot',seasons[i_season],i_lwt)
#        sc = map.scatter(xi,yi,s=20,c=data,vmin=-40,vmax=40,cmap=cmap)#,cmap=plt.cm.jet)#marker='o',color='k')
#        #plt.text(xi[i_site],yi[i_site], site_names[i_site])
#        plt.title((str(lamb_weather_type[i_lwt])), fontsize=15)
#        ax2 = fig.add_axes([0.92, 0.2, 0.02, 0.6])    
#    cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, spacing='proportional', ticks=bounds, boundaries=bounds, format='%1i')
#    cb.set_label('Anomaly', fontsize=15)
#    plt.savefig(str(seasons[i_season]+'_90th_percentile_anomalies.png'))
#    plt.show()

#for i_season in range(n_seasons):
#    fig = plt.figure(figsize=(20, 20))
#    fig.subplots_adjust(hspace=0.05, wspace=0.05)
#    for i_lwt in range(len(lamb_weather_type)-1): 
#        ax = fig.add_subplot(2, 4, i_lwt+1)
#        map = Basemap(projection='merc', lat_0 = 57, lon_0 = -4,
#                      resolution = 'i', area_thresh = 0.05,
#                      llcrnrlon=-12, llcrnrlat=49,
#                      urcrnrlon=4, urcrnrlat=61)
#        map.drawcoastlines(linewidth = 1, zorder = 0)
#        cmap = plt.cm.seismic
#        # extract all colors from the .jet map
#        cmaplist = [cmap(i) for i in range(cmap.N)]
#        # create the new map
#        cmap = cmap.from_list('Custom cmap', cmaplist, cmap.N)
#        # define the bins and normalize
#        bounds = np.linspace(-15,15,31)
#        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
#        
#        data = lwt_anomaly_seasonal[2,i_season,i_lwt,:]
#        #print('data = ', data)
#        #time.sleep(2)
#        xi,yi = map(lons,lats)
#        #print 'lon, lat',  xi, yi
#        print( 'creating plot',seasons[i_season],i_lwt)
#        sc = map.scatter(xi,yi,s=20,c=data,vmin=-40,vmax=40,cmap=cmap)#,cmap=plt.cm.jet)#marker='o',color='k')
#        #plt.text(xi[i_site],yi[i_site], site_names[i_site])
#        plt.title((str(lamb_weather_type[i_lwt])), fontsize=15)
#        ax2 = fig.add_axes([0.92, 0.2, 0.02, 0.6])    
#    cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, spacing='proportional', ticks=bounds, boundaries=bounds, format='%1i')
#    cb.set_label('Anomaly', fontsize=15)
#    plt.savefig(str(seasons[i_season]+'_75th_percentile_anomalies.png'))
#    plt.show()
    
    