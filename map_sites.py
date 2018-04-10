#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 10:39:29 2018

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
from adjustText import adjust_text

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


fig = plt.figure(figsize=(16, 20))
map = Basemap(projection='merc', lat_0 = 57, lon_0 = -4,
              resolution = 'i', area_thresh = 0.05,
              llcrnrlon=-12, llcrnrlat=49,
              urcrnrlon=4, urcrnrlat=61)
map.drawcoastlines(linewidth = 1, zorder = 0)
xi,yi = map(lons,lats)
map.scatter(xi,yi,s=50)
for i_site in range(len(site_names)):
    plt.text(xi[i_site],yi[i_site],site_names[i_site],fontsize=8)
plt.savefig('map_of_site_names.png')
plt.show()



fig = plt.figure(figsize=(16, 20))
map = Basemap(projection='merc', lat_0 = 57, lon_0 = -4,
              resolution = 'i', area_thresh = 0.05,
              llcrnrlon=-12, llcrnrlat=49,
              urcrnrlon=4, urcrnrlat=61)
map.drawcoastlines(linewidth = 1, zorder = 0)
xi,yi = map(lons,lats)
sc = map.scatter(xi,yi,s=50)
for i_site in range(len(site_names)):
    if i_site == 24 or i_site ==30 or i_site == 18 or i_site == 37 or i_site ==31 or i_site == 26 or i_site == 6 or i_site ==38 or i_site == 19: 
        texts = plt.text(xi[i_site],yi[i_site],i_site+1,fontsize=12,fontweight='bold',
                         horizontalalignment='left',verticalalignment='bottom')
    elif i_site == 21 or i_site == 6 or i_site == 25 or i_site == 11 or i_site == 14 or i_site == 0:
        texts = plt.text(xi[i_site],yi[i_site],i_site+1,fontsize=12,fontweight='bold',
                         horizontalalignment='right',verticalalignment='bottom')
    else:
        texts = plt.text(xi[i_site],yi[i_site],i_site+1,fontsize=12,fontweight='bold',
                         horizontalalignment='left',verticalalignment='top')
#adjust_text(texts)
#adjust_text(texts, x=xi, y=yi, autoalign='y',
            #only_move={'points':'y', 'text':'y'}, force_points=0.15,
            #arrowprops=dict(arrowstyle="->", color='r', lw=0.5))
#adjust_text(texts, add_objects=sc, autoalign='xy', expand_objects=(0.1, 1),
#            only_move={'points':'', 'text':'y', 'objects':'y'}, force_text=0.75, force_objects=0.1,
#            arrowprops=dict(arrowstyle="simple, head_width=0.25, tail_width=0.05", color='r', lw=0.5, alpha=0.5))
plt.savefig('map_of_site_numbers.png')          
plt.show()

