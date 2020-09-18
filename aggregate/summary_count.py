# Jinny Park
# A simple script tabulating most frequent item in a csv.
# Includes two functions: 1. creating a duple (artist,title) from a csv file and putting in a list, 2. counting up most common occurences of the duple.
import csv
import os
#csv_dir = os.getcwd()
csv_dir = "/Users/jinnykittiy/Box Sync/DataMining/music_charts/aggregate"
os.chdir(csv_dir)
csv_path = "musicCharts_2010_aggregate_cleanedUp.csv"

duple_list = []
#a function to add fields of artist name and title of songs in a new csv file
#returns [[list of title and artist combined as a single string],[dictionary of title/artist and its index in csv file.]]
def duple_csv_fields(filename):
    # file_name_list = filename.split('.')
    # file_name = file_name_list[0]
    rows = []
    indexes = []
    dict = {}
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.__next__()
        #fields = ["artist", "title", "total streams"]
        index = 1
    #extracting each data row one by one
        for row in csvreader:
            title_and_artist = ""
            artist = ""
            title = ""
            #print(row[0])
            artist = row[0]
            title = row[1]
            title_and_artist = artist + " - " + title
            # print(title_and_artist)
            # print(index)
            # #print("artist is: ", artist, "title is: ",title)
            rows.append(title_and_artist)
            dict[title_and_artist] = index
            #indexes.append(index)
            index = index + 1
        return([rows,dict])

duple_list = duple_csv_fields(csv_path)
#print(duple_list[1])

# count frequencies of items
from collections import Counter
counter = Counter(duple_list[0])

most_common_top_500 = counter.most_common(500)
print(most_common_top_500)
outfile = "summary_2010.txt"


with open(outfile,"w") as text_file:
    for item in most_common_top_500:
        text_file.write(item[0] + ": " + str(item[1]) + "\n")

#print(counter.most_common(100))
