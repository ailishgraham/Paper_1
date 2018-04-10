#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 11:53:36 2018

@author: ee15amg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:47:44 2018

@author: ee15amg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:43:34 2018

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

df = pd.read_csv("/nfs/see-fs-01_teaching/ee15amg/TRAJ_MODEL/AURN_data/complete/post_transfer/raw_data/no2_kerbside_only.csv", usecols=[0,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                         21,22,23,24,25,26,27,28,29])
print df.head()
time.sleep(10)
old_header = ('Date','LWT','Birmingham A4540 Roadside','Birmingham Tyburn Roadside',
              'Bury Roadside','Camden Kerbside','Carlisle Roadside',
              'Chatham Roadside','Chepstow A48','Chesterfield Roadside',
              'Glasgow High Street','Glasgow Kerbside','Haringey Roadside',
              'Leamington Spa Rugby Road','Leeds Headingley Kerbside',
              'London Marylebone Road','Sandy Roadside','Stanford-le-Hope Roadside',
              'Stockton-on-Tees A1305 Roadside','Stockton-on-Tees Eaglescliffe',
              'Storrington Roadside','Swansea Roadside','York Fishergate')

new_header = ('Date', 'LWT','52.477609','52.52194','53.53911','51.54421','54.894834',
              '51.374264','51.638094','53.231722','55.860936','55.85917',
              '51.5993','52.294884','53.819972','51.52253','52.132417',
              '51.518167','54.565819','54.516667','50.916932','51.632696','53.951889')

col_rename_dict = {i:j for i,j in zip(old_header,new_header)}
df.rename(columns=col_rename_dict, inplace=True)
print df.head()
time.sleep(10)
data = df.replace('No data', np.NaN)

uc = [-1]
uc1 = [0]
uc2 = [20]


c = data.loc[(data['LWT']== uc) | (data['LWT']== uc1) | (data['LWT']== uc2)]
print(c)
print type(c)
c.to_csv("binned_no2_kerbside_lats_annual_uc"+".csv", na_rep="NaN", index=False, encoding='utf-8')

ane =[1]
ne =[11]
cne =[21]

c = data.loc[(data['LWT']== ane) | (data['LWT']== ne) | (data['LWT']== cne)]
print(c)
print type(c)
c.to_csv("binned_no2_kerbside_lats_annual_ne"+".csv", na_rep="NaN", index=False, encoding='utf-8')

ae=[2]
e=[12]
ce=[22]

c = data.loc[(data['LWT']== ae) | (data['LWT']== e) | (data['LWT']== ce)]
print(c)
print type(c)
c.to_csv("binned_no2_kerbside_lats_annual_e"+".csv", na_rep="NaN", index=False, encoding='utf-8')


ase=[3]
se=[13]
cse=[23]

c = data.loc[(data['LWT']== ase) | (data['LWT']== se) | (data['LWT']== cse)]
print(c)
print type(c)
c.to_csv("binned_no2_kerbside_lats_annual_se"+".csv", na_rep="NaN", index=False, encoding='utf-8')


a_s=[4]
s=[14]
cs=[24]

c = data.loc[(data['LWT']== a_s) | (data['LWT']== s) | (data['LWT']== cs)]
print(c)
print type(c)
c.to_csv("binned_no2_kerbside_lats_annual_s"+".csv", na_rep="NaN", index=False, encoding='utf-8')


asw=[5]
sw=[15]
csw=[25]

c = data.loc[(data['LWT']== asw) | (data['LWT']== sw) | (data['LWT']== csw)]
print(c)
print type(c)
c.to_csv("binned_no2_kerbside_lats_annual_sw"+".csv", na_rep="NaN", index=False, encoding='utf-8')


aw=[6]
w=[16]
cw=[26]

c = data.loc[(data['LWT']== aw) | (data['LWT']== w) | (data['LWT']== cw)]
print(c)
print type(c)
c.to_csv("binned_no2_kerbside_lats_annual_w"+".csv", na_rep="NaN", index=False, encoding='utf-8')



anw=[7]
nw=[17]
cnw=[27]

c = data.loc[(data['LWT']== anw) | (data['LWT']== nw) | (data['LWT']== cnw)]
print(c)
print type(c)
c.to_csv("binned_no2_kerbside_lats_annual_nw"+".csv", na_rep="NaN", index=False, encoding='utf-8')



an=[8]
n=[18]
cn=[28]

c = data.loc[(data['LWT']== an) | (data['LWT']== n) | (data['LWT']== cn)]
print(c)
print type(c)
c.to_csv("binned_no2_kerbside_lats_annual_n"+".csv", na_rep="NaN", index=False, encoding='utf-8')




