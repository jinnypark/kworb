# Jinny Park
# a simple code to process chart2000 csv files
import csv
import os
#csv_dir = os.getcwd()
csv_dir = "/Users/jinnykittiy/Box Sync/DataMining/music_charts"
file_path = "chart2000-song-2000-decade-0-3-0057.csv"
#file_path = "chart2000-song-2010-decade-0-3-0057.csv"

# chart2000 combines billboard charts and others globally
# in the form of:
# decade,position,artist,song,indicativerevenue,us,uk,de,fr,ca,au
# "2010s","1","Ed Sheeran","Shape Of You","36650.3353832966","1","1","1","1","1","1"

# a function to add fields of artist name and title of songs in a new csv file
def process_csv(filename):
    file_name_list = filename.split('.')
    file_name = file_name_list[0]
    fields = []; rows = []
    line_count = 0
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.__next__()
        fields = ["artist", "title","decade"]

    #extracting each data row one by one
        for row in csvreader:
            newrow = []
            aritst = ""
            title = ""
            decade = ""
        # all I need is decade [0], artist[2] song title[3].
            decade = row[0]
            artist = row[2]
            title = row[3]
            newrow = [decade, artist, title]
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
