# Jinny Park
# a simple code to aggregate csv files of music charts from diff. sources.
import csv
import os
#csv_dir = os.getcwd()

csv_dir_youtube = "/Users/jinnykittiy/Box Sync/DataMining/music_charts/youtube"
chart2000_file_path = "/Users/jinnykittiy/Box Sync/DataMining/music_charts/chart2000-song-2010-decade-0-3-0057_parsed.csv"
spotify_path = "/Users/jinnykittiy/Box Sync/DataMining/music_charts/top1000_spotify_2013-2020_parsed.csv"

# just for youtube files =================
#walk all files in youtube directory to get a list of youtube csv files
os.chdir(csv_dir_youtube)
dir_tree = os.walk(csv_dir_youtube)
for dirpath, dirnames, filenames in dir_tree:
    pass

#filter only 2010s csv file records
csv_list_2010 = []
for file in filenames:
    if file.endswith('_parsed.csv'):
        if file.startswith('top100_youtube_201'):
            csv_list_2010.append(file)
print(csv_list_2010)
#=========================================

#process the file and add a new field that records the decade of the file it comes from.
#merge the resulting rows to a pre-existing csv file.
def process_csv(filename):
    year = ""
    new_file_name = ""
    file_name_list = filename.split('_parsed')
    # ##only for youtube csv files ###=======
    year = file_name_list[0].split("_")[2]
    print(year)
for a_file in csv_list_2010:
    print(a_file)
    process_csv(a_file)

    # ##==============
    fields = []; rows = []
    line_count = 0
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.__next__()
        fields = ["artist", "title", "musicChart", "year/decade"]
        line_count = 1
        artist = ""
        title = ""
        # musicChart = "chart2000"
        musicChart = "YouTube"
        #musicChart = "Spotify"
        yearDecade = year

        #for YouTube ============
        for row in csvreader:
            newrow = []
            artist = row[0]
            title = row[1]
            newrow = [artist,title,musicChart, yearDecade]
            rows.append(newrow)
            #print(newrow)
        # ======================
    # extracting each data row one by one
    # for chart2000, fields are ordered as [decade,artist, title]
    # ====chart2000==========
        # for row in csvreader:
        #     newrow = []
        #     yearDecade = row[0]
        #     artist = row[1]
        #     title = row[2]
        #     newrow = [artist,title,musicChart, yearDecade]
        #     rows.append(newrow)
#            print(newrow)
    # =====================
    # for spotify, fileds are ordered as [artist,title,views,decade]
    #====spotify==========
#         for row in csvreader:
#             newrow = []
#             yearDecade = row[3]
#             artist = row[0]
#             title = row[1]
#             newrow = [artist,title,musicChart, yearDecade]
#             rows.append(newrow)
# #            print(newrow)
    #=====================
    # testing============
        # print(rows)
# test_yt = "top100_youtube_2012_parsed.csv"
# process_csv(test_yt)
    #================
    #path = "/Users/jinnykittiy/Box Sync/DataMining/music_charts"
    #os.chdir(path)
    outfile = '/Users/jinnykittiy/Box Sync/DataMining/music_charts/musicCharts_2010_aggregate.csv'
    #do something to append as new rows to the outfile
    with open(outfile, 'a', newline="") as csvfile:
    #with open(outfile, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        # csvwriter.writerow(fields)
        for row in rows:
            csvwriter.writerow(row)
# run for youtube ======
for a_file in csv_list_2010:
    process_csv(a_file)
#=====
# run it
process_csv(chart2000_file_path)

### itunes, spotify and applemusic are all single csv files. process them individually.
import csv
import os
itunes_path = "/Users/jinnykittiy/Box Sync/DataMining/music_charts/top1000_itunes_2010-2020_parsed.csv"
applemusic_path = "/Users/jinnykittiy/Box Sync/DataMining/music_charts/top1000_appleMusic_2017-2020_parsed.csv"
#os.chdir(itunes_path)
def process_csv_v2(filename):
    year = ""
    musicChart = ""

    file_name_list = filename.split('_')
    #print(file_name_list)
    year = file_name_list[3]
    #musicChart = "Itunes"
    musicChart = "Apple Music"
    #print(year)
#process_csv_v2(applemusic_path)
    fields = []; rows = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.__next__() #don't count the fields
        #fields = ["artist", "title", "musicChart", "year/decade"]
        #artist = [0] title = [1]
        artist = ""
        title = ""
        yearDecade = year
    #extracting each data row one by one
        for row in csvreader:
            newrow = []
            artist = row[0]
            title = row[1]
            newrow = [artist, title,musicChart, yearDecade]
            rows.append(newrow)
            # print(newrow)

    # print(rows)
# process_csv_v2(applemusic_path)
    outfile = '/Users/jinnykittiy/Box Sync/DataMining/music_charts/musicCharts_2010_aggregate.csv'
    #do something to append as new rows to the outfile
    with open(outfile, 'a', newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        #csvwriter.writerow(fields)
        for row in rows:
            csvwriter.writerow(row)
process_csv_v2(applemusic_path)
