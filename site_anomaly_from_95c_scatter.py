#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 15:33:21 2018

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
from matplotlib import colors as mcolors
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

# Set dimensions of array
n_years = (len(data_year))
n_days = (365)
n_sites = (len(df.columns))
#ÃÂprint 'n_years', n_years,'n_days', n_days,'n_sites', n_sites 


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
            #print 'year, site', i_year, i_site
            #print 'array', temp_centile_data_flattened
            good_sites.append(i_site)
            good_years.append(i_year)
            for i_site in range(n_sites):
                for i_day in range(n_days):
                    #print 'year',i_year,'site', i_site,'day', i_day
                    gd_temp_data = data_yearly[i_year,i_site,i_day]
                    #print 'gd_data', gd_temp_data
                    data_yearly_checked[i_year,i_site,i_day] = gd_temp_data
        

## get lwt info for each day and add to array    

    for i_day in range(n_days):
        temp_data_lwt = (data_year_lwt[i_year].iloc[i_day])
        #print 'data selected', temp_data_lwt 
        data_yearly_lwt[i_year,i_day] = float(temp_data_lwt)
#print '0,0',data_yearly_lwt[0,0], '0,1',data_yearly_lwt[0,1], '1,1',data_yearly_lwt[1,1]
#time.sleep(10)
    
## Check what the lists and arrays look like 
        
#print('gy', good_years)
#print('gs', good_sites)
#print('shape data', np.shape(data_yearly_checked), 'shape lwt', np.shape(data_yearly_lwt))
#print('data', data_yearly_checked[:,:,:])
#print('lwt', data_yearly_lwt[:,:])

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
all_data = np.empty([n_years,n_sites,n_days])
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

lamb_weather_type = ['N','NE','E','SE','S','SW','W','NW','all']
n_lwt = len(lamb_weather_type)
lwt_array = np.empty([n_lwt,n_years,n_sites,n_days])
lwt_array[:,:,:,:] = np.nan
n_stats = 5
n_seasons = 4
statistics = np.zeros([n_stats,n_seasons,n_lwt,n_sites])
lwt_anomaly = np.zeros([n_stats,n_seasons,n_lwt,n_sites])
statistics_annual = np.zeros([n_stats,n_lwt,n_sites])
lwt_anomaly_annual = np.zeros([n_stats,n_lwt,n_sites])

for i_year in range(len(data_year)):
    #Look for each lwt occurence in data:
    NE_flow = np.where((data_yearly_lwt[i_year,:] == NE_index[0]) | (data_yearly_lwt[i_year,:] == NE_index[1]) | (data_yearly_lwt[i_year,:] == NE_index[2]))
    E_flow = np.where((data_yearly_lwt[i_year,:] == E_index[0]) | (data_yearly_lwt[i_year,:] == E_index[1]) | (data_yearly_lwt[i_year,:] == E_index[2]))
    SE_flow = np.where((data_yearly_lwt[i_year,:] == SE_index[0]) | (data_yearly_lwt[i_year,:] == SE_index[1]) | (data_yearly_lwt[i_year,:] == SE_index[2]))
    S_flow = np.where((data_yearly_lwt[i_year,:] == S_index[0]) | (data_yearly_lwt[i_year,:] == S_index[1]) | (data_yearly_lwt[i_year,:] == S_index[2]))
    SW_flow = np.where((data_yearly_lwt[i_year,:] == SW_index[0]) | (data_yearly_lwt[i_year,:] == SW_index[1]) | (data_yearly_lwt[i_year,:] == SW_index[2]))
    W_flow = np.where((data_yearly_lwt[i_year,:] == W_index[0]) | (data_yearly_lwt[i_year,:] == W_index[1]) | (data_yearly_lwt[i_year,:] == W_index[2]))
    NW_flow = np.where((data_yearly_lwt[i_year,:] == NW_index[0]) | (data_yearly_lwt[i_year,:] == NW_index[1]) | (data_yearly_lwt[i_year,:] == NW_index[2]))
    N_flow = np.where((data_yearly_lwt[i_year,:] == N_index[0]) | (data_yearly_lwt[i_year,:] == N_index[1]) | (data_yearly_lwt[i_year,:] == N_index[2]))

    
    #Look for all flow types
    all_flow = np.where((data_yearly_lwt[i_year,:] == all_index[0]) | (data_yearly_lwt[i_year,:] == all_index[1]) 
    | (data_yearly_lwt[i_year,:] == all_index[2]) | (data_yearly_lwt[i_year,:] == all_index[3])
    | (data_yearly_lwt[i_year,:] == all_index[4]) | (data_yearly_lwt[i_year,:] == all_index[5]) 
    | (data_yearly_lwt[i_year,:] == all_index[6]) | (data_yearly_lwt[i_year,:] == all_index[7])
    | (data_yearly_lwt[i_year,:] == all_index[8]) | (data_yearly_lwt[i_year,:] == all_index[9])
    | (data_yearly_lwt[i_year,:] == all_index[10]) | (data_yearly_lwt[i_year,:] == all_index[11]) 
    | (data_yearly_lwt[i_year,:] == all_index[12]) | (data_yearly_lwt[i_year,:] == all_index[13])
    | (data_yearly_lwt[i_year,:] == all_index[14]) | (data_yearly_lwt[i_year,:] == all_index[15])
    | (data_yearly_lwt[i_year,:] == all_index[16]) | (data_yearly_lwt[i_year,:] == all_index[17]) 
    | (data_yearly_lwt[i_year,:] == all_index[18]) | (data_yearly_lwt[i_year,:] == all_index[19])
    | (data_yearly_lwt[i_year,:] == all_index[20]) | (data_yearly_lwt[i_year,:] == all_index[21])
    | (data_yearly_lwt[i_year,:] == all_index[22]) | (data_yearly_lwt[i_year,:] == all_index[23]))
   
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
        temp_data_all = data_yearly_checked[i_year,i_site,all_flow]
        print('i_year',i_year, 'i_site', i_site, temp_data_NE)
        
        NE_data[i_year,i_site,NE_flow] = temp_data_NE
        E_data[i_year,i_site,E_flow] = temp_data_E
        SE_data[i_year,i_site,SE_flow] = temp_data_SE
        S_data[i_year,i_site,S_flow] = temp_data_S
        SW_data[i_year,i_site,SW_flow] = temp_data_SW
        W_data[i_year,i_site,W_flow] = temp_data_W
        NW_data[i_year,i_site,NW_flow] = temp_data_NW
        N_data[i_year,i_site,N_flow] = temp_data_N
        all_data[i_year,i_site,all_flow] = temp_data_all

print('N_data', N_data[:,:,:])
print('SE_data', SE_data[:,:,:])
print('SW_data', SW_data[:,:,:])
print('all_data', all_data[:,:,:])
time.sleep(20)

## Fill lwt_array with data for pm25 concs in each lwt
lwt_array[0,:,:,:] = N_data[:,:,:]
lwt_array[1,:,:,:] = NE_data[:,:,:]
lwt_array[2,:,:,:] = E_data[:,:,:]
lwt_array[3,:,:,:] = SE_data[:,:,:]
lwt_array[4,:,:,:] = S_data[:,:,:]
lwt_array[5,:,:,:] = SW_data[:,:,:]
lwt_array[6,:,:,:] = W_data[:,:,:]
lwt_array[7,:,:,:] = NW_data[:,:,:]
lwt_array[8,:,:,:] = all_data[:,:,:]
print('lwt array check',lwt_array[0,:,:,:])
print('lwt array check',lwt_array[3,:,:,:])
time.sleep(5)
# calcaulate stats for each circ at each site for each season
start = [59,151,243,334]
stop = [151,243,334,365] 

for i_season in range(n_seasons):
    #print('start,stop',start[i_season], stop[i_season],'season', i_season)
    #time.sleep(5)
    for i_lwt in range(len(lamb_weather_type)):
        for i_site in range(n_sites):
            #print('circ', i_circ)
            #print('isite', i_site)
            if stop[i_season] == 365:
                d_flattened = np.ndarray.flatten(lwt_array[i_lwt,:, i_site, start[i_season]:stop[i_season]])
                d_flattened1 = np.ndarray.flatten(lwt_array[i_lwt,:, i_site, 0:59])
                d_flattened = np.concatenate([d_flattened,d_flattened1])
                #print('WINTER,iseason',i_season,d_flattened)
                #time.sleep(1)
                centile50 = np.nanpercentile(d_flattened, 50)
                statistics[0,3,i_lwt,i_site]= centile50
                #print('50=', centile50)
                #time.sleep(2)
                centile25 = np.nanpercentile(d_flattened, 25)
                statistics[1,3,i_lwt,i_site]= centile25
                #print('25=', centile25)
                #time.sleep(2)
                centile75 = np.nanpercentile(d_flattened, 75)
                statistics[2,3,i_lwt,i_site]= centile75
                #print('75=', centile75)
                #time.sleep(2)
                centile90 = np.nanpercentile(d_flattened, 90)
                statistics[3,3,i_lwt,i_site]= centile90
                #print('90=', centile90)
                #time.sleep(1)
                centile10 = np.nanpercentile(d_flattened, 10)
                statistics[4,3,i_lwt,i_site]= centile10
                #print('10=', centile10)
        

            else:
                d_flattened = np.ndarray.flatten(lwt_array[i_lwt,:, i_site, start[i_season]:stop[i_season]])
                #print 'i_year', i_year, 
                #print('d flat', d_flattened)
                #print ('non-nans',(np.sum(~np.isnan(d_flattened))))
                #print('len_d', len(d_flattened))
                #print('% data available', (np.sum(~np.isnan(d_flattened))/len(d_flattened)*100))
                centile50 = np.nanpercentile(d_flattened, 50)
                statistics[0,i_season,i_lwt,i_site]= centile50
                #print('50=', centile50)
                #time.sleep(2)
                centile25 = np.nanpercentile(d_flattened, 25)
                statistics[1,i_season,i_lwt,i_site]= centile25
                #print('25=', centile25)
                #time.sleep(2)
                centile75 = np.nanpercentile(d_flattened, 75)
                statistics[2,i_season,i_lwt,i_site]= centile75
                #print('75=', centile75)
                #time.sleep(2)
                centile90 = np.nanpercentile(d_flattened, 90)
                statistics[3,i_season,i_lwt,i_site]= centile90
                #print('90=', centile90)
                #time.sleep(1)
                centile10 = np.nanpercentile(d_flattened, 10)
                statistics[4,i_season,i_lwt,i_site]= centile10
                #print('10=', centile10)

#circ_anomaly = np.zeros([n_stats,n_seasons,n_circ,n_sites])

#Calculate anomalies in each stat value for each season at each site
for i_stat in range(n_stats):    
    for i_season in range(n_seasons):
        for i_lwt in range(len(lamb_weather_type)-1):
            for i_site in range(n_sites):
                print('stat',i_stat,'seas',i_season,'lwt',i_lwt,'site',i_site)
                temp_data_anom = ((statistics[i_stat,i_season,i_lwt,i_site])-(statistics[i_stat,i_season,8,i_site]))
                print('td=',temp_data_anom)
                #time.sleep(2)
                lwt_anomaly[i_stat,i_season,i_lwt,i_site]=temp_data_anom
print('stat lwt',statistics[3,0,0,0],'stat lwt all',statistics[3,0,3,0], 'anom',lwt_anomaly[3,0,0,0])
                


# Do same calculations for annual 
        
for i_lwt in range(len(lamb_weather_type)):
    for i_site in range(n_sites):
        #print('circ', i_circ)
        #print('isite', i_site)
       
            d_flattened = np.ndarray.flatten(lwt_array[i_lwt,:, i_site,:])
            #print 'i_year', i_year, 
            #print('d flat', d_flattened)
            #print ('non-nans',(np.sum(~np.isnan(d_flattened))))
            #print('len_d', len(d_flattened))
            #print('% data available', (np.sum(~np.isnan(d_flattened))/len(d_flattened)*100))
            centile50 = np.nanpercentile(d_flattened, 50)
            statistics_annual[0,i_lwt,i_site]= centile50
            #print('50=', centile50)
            #time.sleep(2)
            centile25 = np.nanpercentile(d_flattened, 25)
            statistics_annual[1,i_lwt,i_site]= centile25
            #print('25=', centile25)
            #time.sleep(2)
            centile75 = np.nanpercentile(d_flattened, 75)
            statistics_annual[2,i_lwt,i_site]= centile75
            #print('75=', centile75)
            #time.sleep(2)
            centile90 = np.nanpercentile(d_flattened, 90)
            statistics_annual[3,i_lwt,i_site]= centile90
            #print('90=', centile90)
            #time.sleep(1)
            centile10 = np.nanpercentile(d_flattened, 10)
            statistics_annual[4,i_lwt,i_site]= centile10
            #print('10=', centile10)
            
            
for i_stat in range(n_stats):    
    for i_lwt in range(len(lamb_weather_type)-1):
        for i_site in range(n_sites):
            print('stat',i_stat,'lwt',i_lwt,'site',i_site)
            temp_data_anom = ((statistics_annual[i_stat,i_lwt,i_site])-(statistics_annual[i_stat,8,i_site]))
            print('td=',temp_data_anom)
            #time.sleep(2)
            lwt_anomaly_annual[i_stat,i_lwt,i_site]=temp_data_anom
print('stat lwt',statistics_annual[3,0,0],'stat lwt all',statistics_annual[3,3,0], 'anom',lwt_anomaly_annual[3,0,0])
            

# Plot annual data too

marker_color = ['b', 'c','darkorange', 'r', 'y', 'g', 'm', 'blueviolet', 'k']
fig, ax = plt.subplots(figsize=(10, 10))
x = range(n_sites)

N_lwt = lwt_anomaly_annual[2,0,:]
NE_lwt = lwt_anomaly_annual[2,1,:]
E_lwt = lwt_anomaly_annual[2,2,:]
SE_lwt = lwt_anomaly_annual[2,3,:]
S_lwt = lwt_anomaly_annual[2,4,:]
SW_lwt = lwt_anomaly_annual[2,5,:]
W_lwt = lwt_anomaly_annual[2,6,:]
NW_lwt = lwt_anomaly_annual[2,7,:]
all_lwt = lwt_anomaly_annual[2,8,:]



ax.plot(x,N_lwt,marker='o', color=marker_color[0], label=(lamb_weather_type[0]))
ax.plot(x,NE_lwt,marker='o', color=marker_color[1], label=(lamb_weather_type[1]))
ax.plot(x,E_lwt,marker='o', color=marker_color[2], label=(lamb_weather_type[2]))
ax.plot(x,SE_lwt,marker='o', color=marker_color[3], label=(lamb_weather_type[3]))
ax.plot(x,S_lwt,marker='o', color=marker_color[4], label=(lamb_weather_type[4]))
ax.plot(x,SW_lwt,marker='o', color=marker_color[5], label=(lamb_weather_type[5]))
ax.plot(x,W_lwt,marker='o', color=marker_color[6], label=(lamb_weather_type[6]))
ax.plot(x,NW_lwt,marker='o', color=marker_color[7], label=(lamb_weather_type[7]))
ax.plot(x,all_lwt, color=marker_color[8], label=(lamb_weather_type[8]))


ax.legend(loc=9, ncol=3, mode="expand", borderaxespad=0.)
#label_lines = mpatches.Patch(color=marker_color[0], label=circ_type[0])
#plt.legend(handles=[label_lines])
plt.title(('Annual 75th percentile anomaly under each LWT 2010-2016'),fontsize=20) 
plt.savefig(('scatter_annual_75th_percentile_under_all_lwt_anomaly.png'))
plt.xlabel('Sites')
plt.ylabel('PM$_{2.5}$ Concentration')
plt.ylim(-8,25)
plt.show()


marker_color = ['b', 'darkorange', 'c', 'r', 'y', 'g', 'm', 'blueviolet', 'k']
fig, ax = plt.subplots(figsize=(10, 10))
x = range(n_sites)

N_lwt = lwt_anomaly_annual[3,0,:]
NE_lwt = lwt_anomaly_annual[3,1,:]
E_lwt = lwt_anomaly_annual[3,2,:]
SE_lwt = lwt_anomaly_annual[3,3,:]
S_lwt = lwt_anomaly_annual[3,4,:]
SW_lwt = lwt_anomaly_annual[3,5,:]
W_lwt = lwt_anomaly_annual[3,6,:]
NW_lwt = lwt_anomaly_annual[3,7,:]
all_lwt = lwt_anomaly_annual[3,8,:]



ax.plot(x,N_lwt,marker='o', color=marker_color[0], label=(lamb_weather_type[0]))
ax.plot(x,NE_lwt,marker='o', color=marker_color[1], label=(lamb_weather_type[1]))
ax.plot(x,E_lwt,marker='o', color=marker_color[2], label=(lamb_weather_type[2]))
ax.plot(x,SE_lwt,marker='o', color=marker_color[3], label=(lamb_weather_type[3]))
ax.plot(x,S_lwt,marker='o', color=marker_color[4], label=(lamb_weather_type[4]))
ax.plot(x,SW_lwt,marker='o', color=marker_color[5], label=(lamb_weather_type[5]))
ax.plot(x,W_lwt,marker='o', color=marker_color[6], label=(lamb_weather_type[6]))
ax.plot(x,NW_lwt,marker='o', color=marker_color[7], label=(lamb_weather_type[7]))
ax.plot(x,all_lwt, color=marker_color[8], label=(lamb_weather_type[8]))


ax.legend(loc=9, ncol=3, mode="expand", borderaxespad=0.)
#label_lines = mpatches.Patch(color=marker_color[0], label=circ_type[0])
#plt.legend(handles=[label_lines])
plt.title(('Annual 90th percentile anomaly under each LWT 2010-2016'),fontsize=20) 
plt.savefig(('scatter_annual_90th_percentile_under_all_lwt_anomaly.png'))
plt.xlabel('Sites')
plt.ylabel('PM$_{2.5}$ Concentration')
plt.ylim(-20,40)
plt.show()



marker_color = ['b', 'c', 'darkorange', 'r', 'y', 'g', 'm', 'blueviolet', 'k']
fig, ax = plt.subplots(figsize=(10, 10))
x = range(n_sites)

N_lwt = lwt_anomaly_annual[0,0,:]
NE_lwt = lwt_anomaly_annual[0,1,:]
E_lwt = lwt_anomaly_annual[0,2,:]
SE_lwt = lwt_anomaly_annual[0,3,:]
S_lwt = lwt_anomaly_annual[0,4,:]
SW_lwt = lwt_anomaly_annual[0,5,:]
W_lwt = lwt_anomaly_annual[0,6,:]
NW_lwt = lwt_anomaly_annual[0,7,:]
all_lwt = lwt_anomaly_annual[0,8,:]



ax.plot(x,N_lwt,marker='o', color=marker_color[0], label=(lamb_weather_type[0]))
ax.plot(x,NE_lwt,marker='o', color=marker_color[1], label=(lamb_weather_type[1]))
ax.plot(x,E_lwt,marker='o', color=marker_color[2], label=(lamb_weather_type[2]))
ax.plot(x,SE_lwt,marker='o', color=marker_color[3], label=(lamb_weather_type[3]))
ax.plot(x,S_lwt,marker='o', color=marker_color[4], label=(lamb_weather_type[4]))
ax.plot(x,SW_lwt,marker='o', color=marker_color[5], label=(lamb_weather_type[5]))
ax.plot(x,W_lwt,marker='o', color=marker_color[6], label=(lamb_weather_type[6]))
ax.plot(x,NW_lwt,marker='o', color=marker_color[7], label=(lamb_weather_type[7]))
ax.plot(x,all_lwt,color=marker_color[8], label=(lamb_weather_type[8]))


ax.legend(loc=9, ncol=3, mode="expand", borderaxespad=0.)
#label_lines = mpatches.Patch(color=marker_color[0], label=circ_type[0])
#plt.legend(handles=[label_lines])
plt.title(('Annual Mean under each LWT 2010-2016'),fontsize=20) 
plt.savefig(('scatter_annual_mean_under_all_lwt_anomaly.png'))
plt.xlabel('Sites')
plt.ylabel('PM$_{2.5}$ Concentration')
plt.ylim(-8,20)
plt.show()