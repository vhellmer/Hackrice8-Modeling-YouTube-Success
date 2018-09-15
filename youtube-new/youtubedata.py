import csv

#row 0 = url tag
#row 1 = yr, day, month trending
#row 2 = video title
#row 3 = channel name
#row 4 = video category (i.e. history, comedy)
#row 5 = detailed date posted
#row 6 = tags
#row 7 = views
with open('USvideos.csv', encoding="utf-8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row[8])
