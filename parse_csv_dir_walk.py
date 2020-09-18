# Jinny Park
# a simple code to parse csv files that combine title and artist in one field
import csv
import os
#csv_dir = os.getcwd()

#csv_dir = "/Users/jinnykittiy/Box Sync/DataMining/music_charts/youtube"
csv_dir = "/Users/jinnykittiy/Box Sync/DataMining/music_charts"
os.chdir(csv_dir)
dir_tree = os.walk(csv_dir)
for dirpath, dirnames, filenames in dir_tree:
    pass

csv_list = []
for file in filenames:
    if file.endswith('.csv'):
        csv_list.append(file)
#print(csv_list)

#a function to add fields of artist name and title of songs in a new csv file
def parse_title(filename):
    file_name_list = filename.split('.')
    file_name = file_name_list[0]
    fields = []; rows = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.__next__()
        fields = ["artist", "title", "total streams"]
        #total streams = [3]
    #extracting each data row one by one
        for row in csvreader:
            newrow = []
            newcol_aritst = ""
            newcol_title = ""
            artist_and_title = []
        # each row looks like this: Katy Perry - Roar (Official),2998634821,671137
            artist_and_title = row[0].split(" - ")
            # make sure the field actually is divisible by " - ". If the list contains anything other than two elements, throw an error.
            if len(artist_and_title) == 2:
                newcol_artist = artist_and_title[0]
                #print("artist is: " + newcol_artist)
                newcol_title = artist_and_title[1]
                #print("title is: " + newcol_title)
            else:
                newcol_artist = row[0]
                newcol_title = "error"
            views = row[4] #as in "total" for appleMusic
            #views = row[4] #as in "total" for itunes
            # avg = "N/A" #not applicable for applemusic or itunes
            newrow = [newcol_artist, newcol_title, views]
            rows.append(newrow)

    # write to a csv file
    outfile = file_name + '_parsed.csv'
    #outfile = filename
    # with open(outfile, 'w', newline="") as csvfile:
    with open(outfile, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        csvwriter.writerow(fields)
        for row in rows:
            csvwriter.writerow(row)
#testing
#parse_title('top100_youtube_2010.csv')
#parse_title('top1000_itunes_2010-2020.csv')
parse_title('top1000_appleMusic_2017-2020.csv')

# #for youtube list of csv files
# for a_file in csv_list:
#     parse_title(a_file)
