#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 10:20:21 2018

@author: ee15amg
"""

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



df = pd.read_csv("/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/raw_data/pm25_kerbside_only.csv", usecols=[0,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                         21,22,23,24,25,26,27,28,29])


#old_header = ('Date', 'LWT', 'Birmingham A4540 Roadside','Birmingham Tyburn Roadside',
#'Bury Roadside','Camden Kerbside','Carlisle Roadside','Chatham Roadside',
#'Chepstow A48','Chesterfield Roadside','Christchurch Barrack Road',
#'Glasgow High Street','Glasgow Kerbside','Greenock A8 Roadside',
#'Haringey Roadside','Leamington Spa Rugby Road','Leeds Headingley Kerbside',
#'London Marylebone Road','Sandy Roadside','Sheffield Barnsley Road',
#'Stanford-le-Hope Roadside','Stockton-on-Tees A1305 Roadside',
#'Stockton-on-Tees Eaglescliffe','Storrington Roadside','Swansea Roadside',
#'York Fishergate')

#new_header = ('Date', 'LWT','57.15736','55.79216','54.59965','51.45258','53.80489',
#        '51.462839','51.48178','53.244131','51.149617','52.411563','55.002818',
#        '50.805778','55.945589','55.865782','53.74878','52.28881','53.80378',
#        '52.619823','51.46603','51.52229','51.45258','51.617333','51.52105',
#        '51.425286','53.48152','54.97825','51.601203','52.614193','52.95473',
#        '51.744806','50.37167','50.82881','53.76559','51.45309','51.45617',
#        '53.48481','53.378622','50.90814','51.544206','53.02821','54.88361',
#        '53.54914','53.37287','53.967513')
#col_rename_dict = {i:j for i,j in zip(old_header,new_header)}
#df.rename(columns=col_rename_dict, inplace=True)
#print df

data = df.replace('No data', np.NaN)

uc = [-1]
uc1 = [0]
uc2 = [20]


c = data.loc[(data['LWT']== uc) | (data['LWT']== uc1) | (data['LWT']== uc2)]
print(c)
print type(c)
c.to_csv("binned_pm25_kerbside_uc"+".csv", na_rep="NaN", index=False, encoding='utf-8')

ane =[1]
ne =[11]
cne =[21]

c = data.loc[(data['LWT']== ane) | (data['LWT']== ne) | (data['LWT']== cne)]
print(c)
print type(c)
c.to_csv("binned_pm25_kerbside_ne"+".csv", na_rep="NaN", index=False, encoding='utf-8')

ae=[2]
e=[12]
ce=[22]

c = data.loc[(data['LWT']== ae) | (data['LWT']== e) | (data['LWT']== ce)]
print(c)
print type(c)
c.to_csv("binned_pm25_kerbside_e"+".csv", na_rep="NaN", index=False, encoding='utf-8')


ase=[3]
se=[13]
cse=[23]

c = data.loc[(data['LWT']== ase) | (data['LWT']== se) | (data['LWT']== cse)]
print(c)
print type(c)
c.to_csv("binned_pm25_kerbside_se"+".csv", na_rep="NaN", index=False, encoding='utf-8')


a_s=[4]
s=[14]
cs=[24]

c = data.loc[(data['LWT']== a_s) | (data['LWT']== s) | (data['LWT']== cs)]
print(c)
print type(c)
c.to_csv("binned_pm25_kerbside_s"+".csv", na_rep="NaN", index=False, encoding='utf-8')


asw=[5]
sw=[15]
csw=[25]

c = data.loc[(data['LWT']== asw) | (data['LWT']== sw) | (data['LWT']== csw)]
print(c)
print type(c)
c.to_csv("binned_pm25_kerbside_sw"+".csv", na_rep="NaN", index=False, encoding='utf-8')


aw=[6]
w=[16]
cw=[26]

c = data.loc[(data['LWT']== aw) | (data['LWT']== w) | (data['LWT']== cw)]
print(c)
print type(c)
c.to_csv("binned_pm25_kerbside_w"+".csv", na_rep="NaN", index=False, encoding='utf-8')



anw=[7]
nw=[17]
cnw=[27]

c = data.loc[(data['LWT']== anw) | (data['LWT']== nw) | (data['LWT']== cnw)]
print(c)
print type(c)
c.to_csv("binned_pm25_kerbside_nw"+".csv", na_rep="NaN", index=False, encoding='utf-8')




an=[8]
n=[18]
cn=[28]

c = data.loc[(data['LWT']== an) | (data['LWT']== n) | (data['LWT']== cn)]
print(c)
print type(c)
c.to_csv("binned_pm25_kerbside_n"+".csv", na_rep="NaN", index=False, encoding='utf-8')



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
    #c.to_csv("binned_pm25_kerbside_"+LWT[i]+".csv", na_rep="NaN", index=False, encoding='utf-8')
    #time.sleep(5)



#print my_df
        


