#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 10:44:10 2018

@author: ee15amg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:16:04 2018

@author: ee15amg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 11:03:08 2018

@author: ee15amg
"""

#!/bin/env python

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import glob, os
import re
import time

filestem = '/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/bin_no2_data/binned_pm25_annual_'
lamb_weather_type = ['n','ne','nw','e','s','se','sw','w','uc']


lats = [57.15736, 55.79216, 54.59965, 52.437165, 53.80489, 51.462839, 51.48178,
        53.244131, 51.149617, 52.411563, 55.002818	, 50.805778, 55.945589, 55.865782,
        53.74878, 52.28881, 53.80378, 52.619823, 51.46603, 51.52229, 51.45258,
        51.617333, 51.52105, 51.425286, 53.48152, 54.97825, 51.601203, 52.614193,
        52.95473, 51.744806, 50.37167, 50.82881, 53.76559, 51.45309, 51.456170,
        53.48481, 53.378622	, 50.90814, 51.544206, 53.02821, 54.88361	, 53.54914, 
        53.37287, 53.967513]

file_list= []
for count in lamb_weather_type:
   fn = filestem+str(count)+'.csv'
   file_list.append( fn )
print(file_list)
# Debug help
###for f in file_list:
###   print f

#n_sites=(len(n_cols))
n_lwt = len(lamb_weather_type)
n_sites = 36
n_correlation = 36
lwt_site_corr = np.zeros([n_lwt,n_sites,n_correlation])




for ilwt in np.arange(len(lamb_weather_type)):
    df = pd.read_csv(file_list[ilwt], index_col=None)
    df = df.replace('No data', np.NaN)
    df = df[df.columns[2:52]]
    df = df.convert_objects(convert_numeric=True)
    #print df
    print 'DF INFO', df.info()
    df1 = df[(df >= 20).any(axis=1)]
    #print 'DF1   ',df1, df1.info()
    #time.sleep(10)
    c = df1.corr(method='spearman') 
    print c
    lwt = c.as_matrix(columns=None)
    print 'LWT', lwt
    print 'shapeLWT', np.shape(lwt), np.size(lwt)
    #print 'lwt0,0', lwt[0,0]
    #print 'lwt0,1', lwt[0,1]
    #print 'lwt0,2', lwt[0,2]
    
    for isite in range(n_sites):
        for i_corr in range(n_correlation):
            print 'isite,icorr,ilwt', isite,i_corr,ilwt
            correl_site = lwt[isite,i_corr]
            print 'correl_site',correl_site
            #time.sleep(1)
            lwt_site_corr[ilwt,isite,i_corr] = correl_site
    print 'array_lwt_site_corr',lwt_site_corr
    time.sleep(10)
    
