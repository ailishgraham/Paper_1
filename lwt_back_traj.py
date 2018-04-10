#!/usr/bin/env python3
# -*- codingi_year,: utf-8 -*-
"""
Created on Fri Mar  2 14:15:40 2018

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

#Read in lwt array for annual checked data 
#Dimensions of array (n_lwt,n_years,n_sites,n_days)
lwt_array = np.load('lwt_pm25_data_checked.npy')
#select 2010-2014 to match back trajectory 
lwt_array = lwt_array[:,0:5,:,:]
print(np.shape(lwt_array))
time.sleep(10)
#Mask nan values where site removed for poor data
lwt_array = np.ma.masked_invalid(lwt_array)

#Read in back trajectory data
#n_sites = 82, n_timesteps = 1464(leap year 4x366),n_timeintervals = 17(4.25 days)
lats_2010 = np.load('back_traj_lats_2010.npy')
lats_2011 = np.load('back_traj_lats_2011.npy')
lats_2012 = np.load('back_traj_lats_2012.npy')
lats_2013 = np.load('back_traj_lats_2013.npy')
lats_2014 = np.load('back_traj_lats_2014.npy')

lons_2010 = np.load('back_traj_lons_2010.npy')
lons_2011 = np.load('back_traj_lons_2011.npy')
lons_2012 = np.load('back_traj_lons_2012.npy')
lons_2013 = np.load('back_traj_lons_2013.npy')
lons_2014 = np.load('back_traj_lons_2014.npy')

print('shape lats',np.shape(lats_2010))
time.sleep(5)
print('shape lwt', np.shape(lwt_array))
time.sleep(5)

#Join separate years of lats and lons together to create array for 2010-2014
lats_backtraj = np.array([lats_2010, lats_2011, lats_2012, lats_2013, lats_2014])
lons_backtraj = np.array([lons_2010, lons_2011, lons_2012, lons_2013, lons_2014])
print('shape joined', np.shape(lats_backtraj))

# Set array dimenions for new back_traj array with same sites as lwt_array
n_traj_sites = 44
n_timesteps = 1464
n_tintervals = 17
n_years_back_traj = 5

n_lwt = 8 
n_years = 5
n_days = 365

#Create array full of nans for back trajectory lats and lons that match lwt_array 
lwt_back_traj_lats = np.empty([n_years_back_traj,n_traj_sites,n_timesteps,n_tintervals])
lwt_back_traj_lats[:,:,:,:]=np.nan
lwt_back_traj_lons = np.empty([n_years_back_traj,n_traj_sites,n_timesteps,n_tintervals])
lwt_back_traj_lons[:,:,:,:]=np.nan

# List of lats in lwt_array
lats = [57.157, 55.792, 54.599, 52.437, 53.804, 51.462, 51.481,
        53.244, 51.149, 52.411, 55.002, 50.805, 55.945, 55.865,
        53.748, 52.288, 53.803, 52.619, 51.466, 51.522, 51.452,
        51.617, 51.521, 51.425, 53.481, 54.978, 51.601, 52.614,
        52.954, 51.744, 50.371, 50.828, 53.765, 51.453, 51.456,
        53.484, 53.378	, 50.908, 51.544, 53.028, 54.883, 53.549, 
        53.372, 53.967] 

lwt_array_sites = [2, 5, 11, 12, 14, 15, 16, 18, 20, 22, 25, 26, 27, 29, 30, 32, 35, 38, 39, 40, 42, 43,
                   0, 1, 5, 11, 12, 16, 18, 19, 21, 22, 25, 27, 28, 31, 33, 37, 39, 40, 42,
                   0, 1, 2, 3, 11, 14, 15, 16, 18, 19, 20, 24, 25, 26, 27, 31, 32, 33, 35, 37, 42, 43,
                   3, 5, 6, 11, 12, 14, 18, 22, 25, 27, 28, 29, 30, 31, 35, 37, 39, 41, 42, 43,
                   2, 3, 6, 14, 15, 16, 17, 19, 24, 26, 31, 35, 37, 39, 43]

#lats_bt = set([ 57.15736, 54.861595, 53.56292, 54.59965, 52.437165, 52.511722, 
#           53.80489, 50.73957, 50.840836, 51.462839, 51.27399, 51.48178, 
#           53.244131, 52.411563, 51.6538, 55.002818, 50.805778, 55.945589,
#           55.865782, 50.792287, 53.74878, 52.28881, 53.80378, 52.619823,
#           51.52229, 51.584128, 51.617333, 51.49633, 51.52105, 51.425286,
#           57.15736, 54.861595, 53.56292, 54.59965, 52.437165, 52.511722,
#           53.80489, 50.73957, 50.840836, 51.462839, 51.27399, 51.48178,
#           53.244131, 52.411563, 51.6538, 55.002818, 50.805778, 55.945589,
#           55.865782, 50.792287, 53.74878, 52.28881, 53.80378, 52.619823,
#           51.52229, 51.584128, 51.617333, 51.49633, 51.52105, 51.425286,
#           57.15736, 54.861595, 53.56292, 54.59965, 52.437165, 52.511722,
#           53.80489, 50.73957, 50.840836, 51.462839, 51.27399, 51.48178,
#           53.244131, 52.411563, 51.6538, 55.002818, 50.805778, 55.945589,
#           55.865782, 50.792287, 53.74878, 52.28881, 53.80378, 52.619823,
#           51.52229, 51.584128, 51.617333, 51.49633, 51.52105, 51.425286,
#           51.49467, 53.48152, 54.97825, 51.601203, 52.271886, 52.614193,
#           52.95473, 51.744806, 55.657472, 50.37167, 50.82881, 53.76559,
#           51.45309, 53.48481, 53.40495, 53.378622, 53.41058, 50.90814,
#           51.544206, 53.02821, 54.88361, 51.47707, 52.605621, 53.54914,
#           53.37287, 53.967513, 52.50385, 55.79216, 55.862281, 51.05625,
#           51.149617, 55.31531, 53.46008, 54.334944, 53.40337, 60.13922,
#           54.43951, 50.7937, 53.326444, 52.554444, 51.781784, 51.45617,
#           52.2944, 51.77798, 57.734456, 52.95049, 52.2985, 50.5976, 56.82266,
#           52.22174, 51.46603, 51.45258])
#def return_indices_of_lats(lats, lats_bt):
#  lats_bt_set = set(lats_bt)
#  return [i for i, v in enumerate(lats) if v in lats_bt_set]
#print( 'backtraj',lats_backtraj[0,:,0,0])
#print( 'lats', lats)
#time.sleep(5)
#print(lats_backtraj[1,:,0,0])
#time.sleep(5)
#print(lats_backtraj[2,:,0,0])
#time.sleep(5)
#print(lats_backtraj[3,:,0,0])
#time.sleep(5)
#print(lats_backtraj[4,:,0,0])
#time.sleep(5)


#loop through years in joined lat_backtraj array to find lats from sites in lwt_array to find lats
lats_found = np.where((lats_backtraj[0,:,0,0] == lats[0]) | (lats_backtraj[0,:,0,0] == lats[1])
| (lats_backtraj[0,:,0,0] == lats[2]) | (lats_backtraj[0,:,0,0] == lats[3])
| (lats_backtraj[0,:,0,0] == lats[4]) | (lats_backtraj[0,:,0,0] == lats[5]) 
| (lats_backtraj[0,:,0,0] == lats[6]) | (lats_backtraj[0,:,0,0] == lats[7])
| (lats_backtraj[0,:,0,0] == lats[8]) | (lats_backtraj[0,:,0,0] == lats[9])
| (lats_backtraj[0,:,0,0] == lats[10]) | (lats_backtraj[0,:,0,0] == lats[11])
| (lats_backtraj[0,:,0,0] == lats[12]) | (lats_backtraj[0,:,0,0] == lats[13])
| (lats_backtraj[0,:,0,0] == lats[14]) | (lats_backtraj[0,:,0,0] == lats[15])
| (lats_backtraj[0,:,0,0] == lats[16]) | (lats_backtraj[0,:,0,0] == lats[17])
| (lats_backtraj[0,:,0,0] == lats[18]) | (lats_backtraj[0,:,0,0] == lats[19])
| (lats_backtraj[0,:,0,0] == lats[20]) | (lats_backtraj[0,:,0,0] == lats[21])
| (lats_backtraj[0,:,0,0] == lats[22]) | (lats_backtraj[0,:,0,0] == lats[23])
| (lats_backtraj[0,:,0,0] == lats[24]) | (lats_backtraj[0,:,0,0] == lats[25])
| (lats_backtraj[0,:,0,0] == lats[26]) | (lats_backtraj[0,:,0,0] == lats[27])
| (lats_backtraj[0,:,0,0] == lats[28]) | (lats_backtraj[0,:,0,0] == lats[29]) 
| (lats_backtraj[0,:,0,0] == lats[30]) | (lats_backtraj[0,:,0,0] == lats[31])
| (lats_backtraj[0,:,0,0] == lats[32]) | (lats_backtraj[0,:,0,0] == lats[33])
| (lats_backtraj[0,:,0,0] == lats[34]) | (lats_backtraj[0,:,0,0] == lats[35])
| (lats_backtraj[0,:,0,0] == lats[36]) | (lats_backtraj[0,:,0,0] == lats[37])
| (lats_backtraj[0,:,0,0] == lats[38]) | (lats_backtraj[0,:,0,0] == lats[39])
| (lats_backtraj[0,:,0,0] == lats[40]) | (lats_backtraj[0,:,0,0] == lats[41])
| (lats_backtraj[0,:,0,0] == lats[42]) | (lats_backtraj[0,:,0,0] == lats[43]))
print('loc lats = ', lats_found)
time.sleep(10)
    #print("lats back traj = ",lats_backtraj[0,lats_found,0,0])
    #time.sleep(2)
    
    #Create new array for back trajectories with only lats and lons from lwt array (19 not 84)
        
temp_data_lats = lats_backtraj[:,lats_found,:,:]
temp_data_lons = lons_backtraj[:,lats_found,:,:]
print('tdl',temp_data_lats[0,:,0,0])
time.sleep(100)
print('shape lats',np.shape(temp_data_lats))
print('shape lons',np.shape(temp_data_lons))
temp_data_lats = np.squeeze(temp_data_lats)
temp_data_lons = np.squeeze(temp_data_lons)
print('shape lats',np.shape(temp_data_lats))
print('shape lons',np.shape(temp_data_lons))
time.sleep(10)  

start = [0,22,41,63,83]
stop = [22,41,63,83,98] 
for i_year in range(n_years):
    begin = (start[i_year])
    end = (stop[i_year])
    data = lwt_array_sites[begin:end]
    for i in range(len(data)):
        print('datai', data[i])
        time.sleep(5)
        #print('tdlats',temp_data_lats[i_year,i,:,:])
        for i_step in range(n_timesteps):
            for i_int in range(n_tintervals):
                td_lats = temp_data_lats[i_year,data[i],i_step,i_int]
                td_lons = temp_data_lons[i_year,data[i],i_step,i_int]
                print('year', i_year, 'data', i, 't_step', i_step, 'int', i_int)
                #print td_lats, td_lons
                #time.sleep(2)
                lwt_back_traj_lats[i_year,data[i],i_step,i_int]=td_lats
                lwt_back_traj_lons[i_year,data[i],i_step,i_int]=td_lons
    #print lwt_array_sites[start[i_year]:stop[i_year]]
print('lats0',lwt_back_traj_lats[0,:,0,0])
print('lons0',lwt_back_traj_lons[0,:,0,0]) 
print('lats1',lwt_back_traj_lats[1,:,0,0])
print('lons1',lwt_back_traj_lons[1,:,0,0])
print('shape lons,lats', np.shape(lwt_back_traj_lats),np.shape(lwt_back_traj_lons)) 
#%%
#n_tinterval_steps = 4
#
#for i_lwt in range(n_lwt):
#    separate_lwt = lwt_array[i_lwt,:,:,:]
#    print('lwt',i_lwt,'separate_lwt',separate_lwt)
#    time.sleep(2)
#    
#    for i_site in range(n_sites_selected):
#        print('i_site',i_site)
#        








#%%

time.sleep(100)
#Plot Back traectories for sites selected
for i_year in range(n_years_back_traj):

    m = Basemap(projection='cyl', llcrnrlat=10, urcrnrlat=65,llcrnrlon=-50, urcrnrlon=50, resolution='c', area_thresh=1000.)
    m.bluemarble()
    m.drawcoastlines(linewidth=0.5)
    m.drawcountries(linewidth=0.5)
    m.drawstates(linewidth=0.5)
    m.drawmapboundary(fill_color='aqua')  
    
    for i_site in range(n_traj_sites): 
        for i_step in range(0,n_timesteps,1):
            print 'i_year',i_year,'i_site',i_site,'i_step',i_step
            temp_traj_lon = lwt_back_traj_lons[i_year,i_site,i_step,:]
            temp_traj_lat = lwt_back_traj_lats[i_year,i_site,i_step,:]
            x, y = m(temp_traj_lon, temp_traj_lat)
            m.plot(x,y,'r-')
    time.sleep(2)
                 
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    #plt.savefig('ifile = '+ str(ifile) + '.png',dpi=200, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None, transparent=False, bbox_inches=None, pad_inches=0.1, frameon=None)
    plt.show()  
    time.sleep(10)         













#%%
for i_step in range(0,n_timesteps,1):

    m = Basemap(projection='cyl', llcrnrlat=10, urcrnrlat=65,llcrnrlon=-50, urcrnrlon=50, resolution='c', area_thresh=1000.)
    m.bluemarble()
    m.drawcoastlines(linewidth=0.5)
    m.drawcountries(linewidth=0.5)
    m.drawstates(linewidth=0.5)
    m.drawmapboundary(fill_color='aqua')  
    
    for i_site in range(n_traj_sites):  
        for i_year in range(n_years_back_traj):
            print 'i_step',i_step,'i_site',i_site,'i_year',i_year
            time.sleep(2)
            temp_traj_lon = lwt_back_traj_lons[i_year,i_site,i_step,:]
            temp_traj_lat = lwt_back_traj_lats[i_year,i_site,i_step,:]
            x, y = m(temp_traj_lon, temp_traj_lat)
            m.plot(x,y,'r-')
        
                 
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    #plt.savefig('ifile = '+ str(ifile) + '.png',dpi=200, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None, transparent=False, bbox_inches=None, pad_inches=0.1, frameon=None)
    plt.show()  
    time.sleep(10)         



    



    
                

