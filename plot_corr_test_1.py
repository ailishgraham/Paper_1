#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 12:55:51 2018

@author: ee15amg
"""

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
from matplotlib import cm as cm
import glob, os
import re
import time

filestem = '/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/correl_data/binned_pm25_spring_lats'
lamb_weather_type = ['n','ne','nw','e','s','se','sw','w','uc']




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
n_sites = 46
n_correlation = 46
lwt_site_corr = np.zeros([n_lwt,n_sites,n_correlation])




for ilwt in np.arange(len(lamb_weather_type)):
    df = pd.read_csv(file_list[ilwt], index_col=None)
    df = df.replace('No data', np.NaN)
    df = df[df.columns[2:52]]
    sorted_df = df.sort_index(axis=1)
    df = sorted_df.convert_objects(convert_numeric=True)
    #print df
    print 'DF INFO', df.info()
    df1 = df[(df >= 25).any(axis=1)]
    #print 'DF1   ',df1, df1.info()
    b = df1.corr(method='spearman')
    print 'B',b
    time.sleep(1)
    df2 = df1.dropna(axis=1, how='all', thresh=None, subset=None, inplace=False)
    c = df2.corr(method='spearman') 
    print 'C',c
    time.sleep(1)
    
    
    plt.figure(figsize=(10, 10))
    plt.imshow(c, cmap='RdYlGn', interpolation='none', aspect='auto')
    plt.colorbar()
    plt.xticks(range(len(c)), c.columns, rotation='vertical')
    plt.yticks(range(len(c)), c.columns)
    plt.gca().invert_yaxis()
#    plt.xticks(range(len(c)), ascending_lats, rotation='vertical')
#    plt.yticks(range(len(c)), descending_lats)
        # Add colorbar, make sure to specify tick locations to match desired ticklabels
        #fig.colorbar(cax, ticks=[.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0])
    plt.title('Correlation of Spring PM$_{2.5}$ at sites during LWT - '+str(lamb_weather_type[ilwt]))
    plt.xlabel('Site')
    plt.ylabel('Site')
    plt.tight_layout()
    plt.savefig('correlate_pm25_spring_sites_nona_'+str(lamb_weather_type[ilwt]))
    #plt.savefig('correlation_spring_pm25_sites_lwt_'+str(lamb_weather_type[ilwt]))
    plt.show()
    

    #correlation_matrix(df)
