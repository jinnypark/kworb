# Author: Jinny Park
# Saving data for music charts from kworb.net using pandas, a simple static html site.
# 02/04/2020
#for itunes worldwide chart since 08/10
# for apple music since 07/17

import pandas as pd
page_domain = 'https://kworb.net/ww/totals.html'
page_domain2 = 'https://kworb.net/apple_songs/totals.html'

#this is a simple webpage with clear labels for the table structure. simply read html using pandas.
dfs = pd.read_html(page_domain2) # returns a list with one elements of pandas dataframe
df = dfs[0] #pandas dataframe element

#only take top 1000
top1000 = df.loc[:999]
top1000.to_csv('top1000_appleMusic_2017-2020' + '.csv', index = False)
