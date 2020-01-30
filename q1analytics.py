#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 20:05:37 2019

@author: Macintosh
"""

import os
#change working directory to external drive
dir = '/Volumes/ExternalHD/JobSearch/Interviews/Moloco'
os.chdir(dir)
os.getcwd()


import pandas as pd

df = pd.read_csv('Q1Analytics.csv')
df.head()
df.shape
df.info()


#1. unique user_id group by site_id
import datetime
from datetime import date

bdv_df = df[df['country_id'] == 'BDV']
bdv_df.shape
bdv_df.groupby(['site_id']).user_id.nunique()

#2. Find users visited a site more than 10 times between 2019-02-03 00:00:00 and 2019-02-04 23:59:59
df['ts_dt'] = pd.to_datetime(df['ts'])

i = pd.date_range(start='2019-02-03 00:00:00', end='2019-02-05 23:59:59')
i
feb_df = df.loc[(df['ts_dt'] >= i[0]) & (df['ts_dt'] < i[2])]

x = feb_df.groupby(['site_id']).user_id.value_counts()
x[x > 10]

#3. Unique num users who visited the site last
# get the last datetime of each user
user_last_visits = df.groupby(['user_id'], as_index=False).ts_dt.max()
user_last_visits.shape
# combine user_id and datetime as a key for filter
user_last_visits['key'] = user_last_visits['user_id']+user_last_visits['ts_dt'].astype(str)
df['key'] = df['user_id']+df['ts']
# get the site_id information of the last visits of users
df_user_last_visist = df[df['key'].isin(user_last_visits['key'])]
df_user_last_visist.groupby(['site_id']).user_id.nunique().sort_values(ascending=False)


#4. Number of users whose first and last sitesvisited are the same

user_1st_visits = df.groupby(['user_id'], as_index=False).ts_dt.min()
user_last_visits = df.groupby(['user_id'], as_index=False).ts_dt.max()

user_1st_visits['key'] = user_1st_visits['user_id']+user_1st_visits['ts_dt'].astype(str)
user_last_visits['key'] = user_last_visits['user_id']+user_last_visits['ts_dt'].astype(str)

df_user_1st_visist = df[df['key'].isin(user_1st_visits['key'])]
df_user_last_visist = df[df['key'].isin(user_last_visits['key'])]

df_1st_visist = df_user_1st_visist[['user_id','site_id']]
df_last_visist = df_user_last_visist[['user_id','site_id']]

# rename the site_id of 1st visit
df_1st_visist.rename(columns={'site_id':'1st_site_id'}, inplace=True)
# merge the 1sta nd last visit dataframe
df_visits = pd.merge(df_1st_visist,df_last_visist, how='inner', left_on='user_id', right_on='user_id')

df_visits[df_visits['1st_site_id'] == df_visits['site_id']].shape[0]
