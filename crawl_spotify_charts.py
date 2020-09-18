# Author: Jinny Park
# Saving data for music charts from kworb.net using pandas, a simple static html site.
# 02/04/2020
# From Spotify, aggregated global charts from 2013/09 to 2020/01.

import pandas as pd

page_domain = 'https://kworb.net/spotify/country/global_weekly_totals.html'

#this is a simple webpage with clear labels for the table structure. simply read html using pandas.

dfs = pd.read_html(page_domain) # returns a list with one elements of pandas dataframe
df = dfs[0] #pandas dataframe element

#only take top 1000
top1000 = df.loc[:1000]
top1000.to_csv('top1000_spotify_2013-2020' + '.csv', index = False)
