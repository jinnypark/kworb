# Author: Jinny Park
# Saving data for music charts from kworb.net using pandas, a simple static html site.
# 02/04/2020

import pandas as pd

#for YouTube most viewed music videos by year
#https://kworb.net/youtube/topvideos_published_2010.html
#https://kworb.net/youtube/topvideos_published_earlier.html
page_domain = 'https://kworb.net/youtube/topvideos_published_'
year = 'earlier' #pre2010
#year = '2010'
suffix = '.html'

#this is a simple webpage with clear labels for the table structure. simply read html using pandas.
yt_url = (page_domain + year + suffix )
dfs = pd.read_html(yt_url) # returns a list with one elements of pandas dataframe
df = dfs[0] #pandas dataframe element

#only take top 100 for each year
#top100 = df.loc[:99]
#top100.to_csv('top100_youtube_' + year + '.csv', index = False)

df.to_csv('top500_youtube_' + 'before_2010' + '.csv', index = False)
