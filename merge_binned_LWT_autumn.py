#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:02:12 2018

@author: ee15amg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:01:12 2018

@author: ee15amg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 15:27:06 2018

@author: ee15amg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 15:17:28 2018

@author: ee15amg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:13:05 2017

@author: ee15amg
"""
 
import pandas as pd
from pandas import DataFrame as frame
import numpy as np
import csv 
from operator import itemgetter, attrgetter
import glob, os
import time
import datetime


n_LWT = 9
n_days = len(data)
n_sites = 44

#pm_lwt = [n_LWT]
pm_lwt_info = np.empty([n_LWT])
#pm_LWT_info = np.empty([n_LWT,n_sites,n_days])

#a = pd.read_csv("LWT_2010_2016.csv")
#b = pd.read_csv("pm25_2010_2016.csv")
#b = b.dropna(axis=1)
#merged = a.merge(b, on='Date')
#merged.to_csv("lwt_pm25.csv", index=False)


df = pd.read_csv("no2_data_autumn.csv", usecols=[0,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                         21,22,23,24,25,26,27,28,29,30,31,32,33,
                                         34,35,36,37,38,39,40,41,42,43,44,45,46,
                                         47,48,49,50])


data = df.replace('No data', np.NaN)

uc = [-1]
uc1 = [0]
uc2 = [20]


c = data.loc[(data['LWT']== uc) | (data['LWT']== uc1) | (data['LWT']== uc2)]
print(c)
print type(c)
c.to_csv("binned_no2_autumn_uc"+".csv", na_rep="NaN", index=False, encoding='utf-8')

ane =[1]
ne =[11]
cne =[21]

c = data.loc[(data['LWT']== ane) | (data['LWT']== ne) | (data['LWT']== cne)]
print(c)
print type(c)
c.to_csv("binned_no2_autumn_ne"+".csv", na_rep="NaN", index=False, encoding='utf-8')

ae=[2]
e=[12]
ce=[22]

c = data.loc[(data['LWT']== ae) | (data['LWT']== e) | (data['LWT']== ce)]
print(c)
print type(c)
c.to_csv("binned_no2_autumn_e"+".csv", na_rep="NaN", index=False, encoding='utf-8')


ase=[3]
se=[13]
cse=[23]

c = data.loc[(data['LWT']== ase) | (data['LWT']== se) | (data['LWT']== cse)]
print(c)
print type(c)
c.to_csv("binned_no2_autumn_se"+".csv", na_rep="NaN", index=False, encoding='utf-8')


a_s=[4]
s=[14]
cs=[24]

c = data.loc[(data['LWT']== a_s) | (data['LWT']== s) | (data['LWT']== cs)]
print(c)
print type(c)
c.to_csv("binned_no2_autumn_s"+".csv", na_rep="NaN", index=False, encoding='utf-8')


asw=[5]
sw=[15]
csw=[25]

c = data.loc[(data['LWT']== asw) | (data['LWT']== sw) | (data['LWT']== csw)]
print(c)
print type(c)
c.to_csv("binned_no2_autumn_sw"+".csv", na_rep="NaN", index=False, encoding='utf-8')


aw=[6]
w=[16]
cw=[26]

c = data.loc[(data['LWT']== aw) | (data['LWT']== w) | (data['LWT']== cw)]
print(c)
print type(c)
c.to_csv("binned_no2_autumn_w"+".csv", na_rep="NaN", index=False, encoding='utf-8')



anw=[7]
nw=[17]
cnw=[27]

c = data.loc[(data['LWT']== anw) | (data['LWT']== nw) | (data['LWT']== cnw)]
print(c)
print type(c)
c.to_csv("binned_no2_autumn_nw"+".csv", na_rep="NaN", index=False, encoding='utf-8')




an=[8]
n=[18]
cn=[28]

c = data.loc[(data['LWT']== an) | (data['LWT']== n) | (data['LWT']== cn)]
print(c)
print type(c)
c.to_csv("binned_no2_autumn_n"+".csv", na_rep="NaN", index=False, encoding='utf-8')



#%%

a = [-1,1,2,3,4,5,6,7,8]
n = [0,11,12,13,14,15,16,17,18]
c = [20,21,22,23,24,25,26,27,28]
LWT = ['uc','ne', 'e', 'se', 's', 'sw', 'w', 'nw', 'w']

for i in range(n_LWT):
    print a[i],n[i],c[i],LWT[i]
    c = data.loc[(data['LWT']== a[i])]
    print c
#    time.sleep(10)
#    c = data.loc[(data['LWT']== a[i]) | (data['LWT']== n[i]) | (data['LWT']== c[i])]
#    print(c)
#    print type(c)
    #c.to_csv("binned_no2_autumn_"+LWT[i]+".csv", na_rep="NaN", index=False, encoding='utf-8')
    #time.sleep(5)



#print my_df
        


