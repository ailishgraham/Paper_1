#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 08:38:49 2018

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
lwt_array = np.load('lwt_pm25_data_checked.npy')
lwt_array = np.ma.masked_invalid(lwt_array)

#Check dimensions and data (array is n_lwt,n_years,n_sites,n_days)
print(np.size(lwt_array))
print(np.shape(lwt_array))
print(lwt_array[:,:,:,:])