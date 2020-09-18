# Author: Jinny Park
# Saving data for music charts from wikipedia billboard chart page using pandas
# 02/04/2020

import pandas as pd

#for YouTube most viewed music videos by year, from 2000-2020.
#https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2000
page_domain = 'https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_'
year = '2019'

#this is a simple webpage with clear labels for the table structure. simply read html using pandas.
url = (page_domain + year)
dfs = pd.read_html(url) # returns a list with one elements of pandas dataframe
df = dfs[0] #pandas dataframe element that contain top 100 data
print(df)

#write it as a csv file
df.to_csv('top100_billboard_' + year + '.csv', index = False)
