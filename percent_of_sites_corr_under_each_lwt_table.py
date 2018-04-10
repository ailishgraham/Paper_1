#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:00:49 2018

@author: ee15amg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:07:06 2018

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

site_names_save = ['Aberdeen','Auchencorth_Moss','Belfast_Centre','Birmingham_Acocks_Green',
              'Blackpool_Morton','Bristol_St_Pauls','Cardiff_Centre','Chesterfield_Loundsley_Green',
              'Chilbolton_Observatory','Coventry_Allesley','Derry_Rosemount','Eastbourne',
              'Edinburgh_St_Leonards','Glasgow_Townhead','Hull_Freetown','Leamington_Spa',
              'Leeds_Centre','Leicester_University','London_Bexley','London_Bloomsbury',
              'London_Eltham','London_Harrow_Stanmore','London_N_Kensington',
              'London_Teddington_Bushy_Park','Manchester_Piccadilly','Newcastle_Centre',
              'Newport','Norwich_Lakenfields','Nottingham_Centre','Oxford_St_Ebbes',
              'Plymouth_Centre','Portsmouth','Preston','Reading_New_Town','Rochester_Stoke',
              'Salford_Eccles','Sheffield_Devonshire_Green','Southampton_Centre',
              'Southend_on_Sea','Stoke_on_Trent_Centre','Sunderland_Silksworth',
              'Wigan_Centre','Wirral_Tranmere','York_Bootham']

#Define dimenisons to loop through for correlation 
lamb_weather_type = ['N','NE','E','SE','S','SW','W','NW']
n_lwt = len(lamb_weather_type)
n_sites = 44
n_corr_coeff = np.empty([n_lwt,n_sites,n_sites])

#Correlate each site with all the others under each lwt
counter = 0
while counter < 44:
    #print 'counter', counter 
    for i_lwt in range(len(lamb_weather_type)):
        #print 'lwt', i_lwt
        for i_site in range(n_sites):
            #print('lwt', i_lwt, 'i_site', i_site, 'counter', counter)
            selected_site = lwt_array[i_lwt,:,counter,:]
            other_sites = lwt_array[i_lwt,:,i_site,:]
            #print('selected_site', selected_site)
            #print('other_sites',other_sites)
            #time.sleep(2)
            selected_site_flat = np.ndarray.flatten(selected_site)
            other_sites_flat = np.ndarray.flatten(other_sites)
            temp_data_corr = np.ma.corrcoef(selected_site_flat,other_sites_flat)
            #print 'corr = ', temp_data_corr[0,1]
            n_corr_coeff[i_lwt,counter,i_site]=temp_data_corr[0,1]
    counter = counter +1
    
#check correlation array   
print n_corr_coeff[0,0,:]
print n_corr_coeff[0,1,:]
time.sleep(2)

#lwt = []
#site_to_corr = []
#corr_with = []
#corr_score = []


#Calculate % of sites correlated with each site
site = []
lwt_code = []
#site_corr_number = []
counter = 0 
while counter < 44:
    site_corr_number = []
    for i_lwt in range(len(lamb_weather_type)): 
        site_counter = 0
        lwt = []
        site_to_corr = []
        corr_with = []
        corr_score = []
        for i_site in range(n_sites):
            if n_corr_coeff[i_lwt,counter,i_site] > 0.8 and n_corr_coeff[i_lwt,counter,i_site] < 0.999999999999999:
                #print( 'i_lwt', i_lwt, 'site', site_names[counter],
                      #'corr with', site_names[i_site], 'corr score', 
                      #n_corr_coeff[i_lwt,counter,i_site])
                site_counter = site_counter + 1
                lwt.append(i_lwt)
                site_to_corr.append(site_names[counter])
                corr_with.append(site_names[i_site])
                corr_score.append(n_corr_coeff[i_lwt,counter,i_site])
        #print('site counter', site_counter)
        site.append(counter)
        site_corr_number.append((float(len(corr_with))/float(44)*100))
    print('site',counter,'corr_number',site_corr_number)
    time.sleep(3)
    counter = counter + 1
#print(lwt)
#print(site_to_corr)
#print(corr_with)
#print(corr_score)







