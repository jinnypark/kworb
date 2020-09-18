# Jinny Park
# a simple code to clean up csv files that encodes extra quotation marks
import csv
import os

files = [
'top100_billboard_2000.csv','top100_billboard_2001.csv','top100_billboard_2002.csv','top100_billboard_2003.csv','top100_billboard_2004.csv','top100_billboard_2005.csv','top100_billboard_2006.csv','top100_billboard_2007.csv','top100_billboard_2008.csv','top100_billboard_2009.csv','top100_billboard_2010.csv','top100_billboard_2011.csv','top100_billboard_2012.csv',
'top100_billboard_2013.csv','top100_billboard_2014.csv','top100_billboard_2015.csv','top100_billboard_2016.csv','top100_billboard_2017.csv','top100_billboard_2018.csv','top100_billboard_2019.csv',
]

filename = 'top100_billboard_2000.csv'
#initializing the titles nad rows list

def erase_quotes(filename):
    file_name_list = filename.split('.')
    file_name = file_name_list[0]
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
                newrow.append(newcol)
            rows.append(newrow)

    #overwrite to a csv file
    outfile = file_name + '_clean.csv'
    with open(outfile, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        csvwriter.writerow(fields)
        for row in rows:
            csvwriter.writerow(row)

for a_file in files:
    erase_quotes(a_file)

#print first 5 rows as a test
for row in rows[:5]:
    for col in row:
        print(col)
    print('\n')
