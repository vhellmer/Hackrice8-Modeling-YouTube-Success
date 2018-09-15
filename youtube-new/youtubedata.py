import csv

#row 0 = url tag
#row 1 = yr, day, month trending
#row 2 = video title
#row 3 = channel name
#row 4 = video category (i.e. history, comedy)
#row 5 = detailed date posted
#row 6 = tags
#row 7 = views
#row 8 = likes
#row 9 = dislikes
#row 10 = comment count
#row 11 = thumbnail link
#row 12, 13, 14 = booleans comments_disabled, ratings_disabled, video_error_or_removed
#row 15 = description

with open('USvideos.csv', encoding="utf-8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #nums = [''.join([c for c in i if c.isdigit()]) for i in data] #extract only the numbers from lines
    #sortedlist = sorted(readCSV, key=lambda row: float(row[7]), reverse=True)
    for row in readCSV:
    	print(row[7])
