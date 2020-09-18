# Jinny Park
# a simple code to process spotify csv files
import csv
import os
#csv_dir = os.getcwd()
csv_dir = "/Users/jinnykittiy/Box Sync/DataMining/music_charts"
file_path = "top1000_spotify_2013-2020.csv"
# a function to add fields of artist name and title of songs in a new csv file

# spotify aggregates charts from 2013-2020.
# Pos,Artist and Title,Wks,T10,Pk,(x?),PkStreams,Total
# 1,Ed Sheeran - Shape of You,160,34.0,1,(x14),64217796,2397753371

def process_csv(filename):
    file_name_list = filename.split('.')
    file_name = file_name_list[0]
    fields = []; rows = []
    line_count = 0
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.__next__()
        fields = ["artist","title","views","decade"]
        year = "2013-2020"
    #extracting each data row one by one
        for row in csvreader:
            newrow = []
            newcol_aritst = ""
            newcol_title = ""
            artist_and_title = []
        # each row looks like this: Katy Perry - Roar (Official),2998634821,671137
            artist_and_title = row[1].split(" - ")
            # make sure the field actually is divisible by " - ". If the list contains anything other than two elements, throw an error.
            if len(artist_and_title) == 2:
                newcol_artist = artist_and_title[0]
                #print("artist is: " + newcol_artist)
                newcol_title = artist_and_title[1]
                #print("title is: " + newcol_title)
            else:
                newcol_artist = row[1]
                newcol_title = "error"
            views = row[6] #as in "total" streams for spotify

            newrow = [newcol_artist, newcol_title, views, year]
            rows.append(newrow)

    # write to a csv file
    outfile = file_name + '_parsed.csv'
    with open(outfile, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        csvwriter.writerow(fields)
        for row in rows:
            csvwriter.writerow(row)
#run it
process_csv(file_path)
