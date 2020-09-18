# Jinny Park
# a simple code to clean up csv files that encodes extra quotation marks
import csv
import os
#csv_dir = os.getcwd()

csv_dir = "/Users/jinnykittiy/Box Sync/DataMining/music_charts/youtube"
os.chdir(csv_dir)
dir_tree = os.walk(csv_dir)
for dirpath, dirnames, filenames in dir_tree:
    pass

csv_list = []
for file in filenames:
    if file.endswith('.csv'):
        csv_list.append(file)
print(csv_list)

#a function to clean up quotes in csv files
def erase_quotes(filename):
    #file_name_list = filename.split('.')
    #file_name = file_name_list[0]
    fields = []; rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.__next__()

    #extracting each data row one by one
        for row in csvreader:
            newcol = ""
            newrow = []
        # reads each row like this: ['1', '"Breathe"', 'Faith Hill']
            for col in row:
                newcol = col.strip('"')
                print(newcol)
                newrow.append(newcol)
            rows.append(newrow)

    #overwrite to a csv file
    #outfile = file_name + '_clean.csv'
    #outfile = filename
    # with open(outfile, 'w', newline="") as csvfile:
    with open(filename, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        csvwriter.writerow(fields)
        for row in rows:
            csvwriter.writerow(row)

for a_file in csv_list:
    erase_quotes(a_file)
