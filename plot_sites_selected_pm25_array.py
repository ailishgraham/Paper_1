#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 13:21:26 2018

@author: ee15amg
"""

from mpl_toolkits.basemap import Basemap
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
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
lwt_array = np.load('lwt_pm25_data_checked.npy')
lwt_array = np.ma.masked_invalid(lwt_array)
#Check dimensions and data (array is n_lwt,n_years,n_sites,n_days)
#print np.size(lwt_array)
print np.shape(lwt_array)
#print lwt_array[:,:,:,:]

#List of lats, lons and names of sites
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
site_names = ['Aberdeen','Auchencorth Moss','Belfast Centre','Birmingham_Acocks_Green',
              'Blackpool Morton','Bristol St Pauls','Cardiff Centre','Chesterfield Loundsley Green',
              'Chilbolton Observatory','Coventry Allesley','Derry Rosemount','Eastbourne',
              'Edinburgh St Leonards','Glasgow Townhead','Hull Freetown','Leamington Spa',
              'Leeds Centre','Leicester University','London Bexley','London Bloomsbury',
              'London Eltham','London Harrow Stanmore','London N Kensington',
              'London Teddington Bushy Park','Manchester Piccadilly','Newcastle Centre',
              'Newport','Norwich Lakenfields','Nottingham Centre','Oxford St Ebbes',
              'Plymouth Centre','Portsmouth','Preston','Reading New Town','Rochester Stoke',
              'Salford Eccles','Sheffield Devonshire Green','Southampton Centre',
              'Southend on Sea','Stoke on Trent Centre','Sunderland Silksworth',
              'Wigan Centre','Wirral Tranmere','York Bootham']

n_lwt = 8
n_years = 7 
n_sites = 44
n_days = 365

print np.size(lwt_array[:,0,0,:])

for i_year in range(n_years):
    fig, ax = plt.subplots(figsize=(16, 20))
    map = Basemap(projection='merc', lat_0 = 57, lon_0 = -4,
                  resolution = 'i', area_thresh = 0.05,
                  llcrnrlon=-12, llcrnrlat=49,
                  urcrnrlon=4, urcrnrlat=61)
    map.drawcoastlines(linewidth = 1, zorder = 0)
    for i_site in range(n_sites):
        data = lwt_array[:,i_year,i_site,:]
        count = np.ma.count_masked(data)
        print('count = ',count)
        if count < 2920: 
            print('year', i_year, 'site', i_site)
            #time.sleep(2)
            xi,yi = map(lons[i_site],lats[i_site])
            sc = map.scatter(xi,yi,s=80)
            plt.text(xi,yi,i_site+1,fontsize=12,fontweight='bold',
                         horizontalalignment='left',verticalalignment='bottom')
    plt.title('Year ' +str(i_year)+' sites selected annual array',fontsize=20)
    plt.savefig('Year_'+str(i_year)+'_annual_array_sites_selected_numbers.png')
    plt.show()

            

for i_year in range(n_years):
    fig, ax = plt.subplots(figsize=(16, 20))
    map = Basemap(projection='merc', lat_0 = 57, lon_0 = -4,
                  resolution = 'i', area_thresh = 0.05,
                  llcrnrlon=-12, llcrnrlat=49,
                  urcrnrlon=4, urcrnrlat=61)
    map.drawcoastlines(linewidth = 1, zorder = 0)
    for i_site in range(n_sites):
        data = lwt_array[:,i_year,i_site,:]
        count = np.ma.count_masked(data)
        print('count = ',count)
        if count < 2920: 
            print('year', i_year, 'site', i_site)
            #time.sleep(2)
            xi,yi = map(lons[i_site],lats[i_site])
            sc = map.scatter(xi,yi,s=80)
            plt.text(xi,yi,site_names[i_site],fontsize=8,
                     horizontalalignment='left',verticalalignment='bottom')
    plt.title('Year ' +str(i_year)+' sites selected annual array',fontsize=20)
    plt.savefig('Year_'+str(i_year)+'_annual_array_sites_selected_names.png')
    plt.show()
        
        
        
        
        
#        #%%
#        fig, ax = plt.subplots(figsize=(16, 20))
#        map = Basemap(projection='merc', lat_0 = 57, lon_0 = -4,
#                      resolution = 'i', area_thresh = 0.05,
#                      llcrnrlon=-12, llcrnrlat=49,
#                      urcrnrlon=4, urcrnrlat=61)
#        map.drawcoastlines(linewidth = 1, zorder = 0)
#        data = lwt_array
#        print('data = ', data)
#        xi,yi = map(lons,lats)
#        #print 'lon, lat',  xi, yi
#        print( 'creating plot')
#        sc = map.scatter(xi,yi,s=60,c=data,vmin=-1,vmax=1,cmap=cmap)#,cmap=plt.cm.jet)#marker='o',color='k')
#        plt.text(xi[i_site],yi[i_site], site_names[i_site],fontsize=12,fontweight='bold')
#        ax2 = fig.add_axes([0.95, 0.1, 0.03, 0.8])
#        cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, spacing='proportional', ticks=bounds, boundaries=bounds, format='%.1f')
#        cb.set_label('Correlation', fontsize=20)
#
##        cb = plt.colorbar(sc)
##        cb.ax.set_yticklabels(cb.ax.get_yticklabels(), fontsize=20)
##        cb.set_label('Pearson Correlation Coefficient', fontsize=20)
#        plt.title('Correlation between '+str(site_names[i_site])+' and all other sites - LWT ' + str(lamb_weather_type[i_lwt]), loc='right',fontsize=15) 
#        plt.savefig('correlation_'+str(site_names_save[i_site])+'_lwt_'+str(lamb_weather_type[i_lwt])+'.png')
#        #plt.savefig('corr_test.png')
#        plt.show()
#        time.sleep(5)