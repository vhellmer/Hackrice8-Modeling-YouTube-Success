from requests import get
import requests
from lxml import html
import csv
from datetime import datetime
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from contextlib import closing
import csv
from collections import defaultdict



###################################################################################
# Helper Functions
###################################################################################

def stringtoint(stringdate):
    """
    split mm/dd/yyyy into year, month and day
    """
    first = stringdate.split("T")[0]
    second = first.split("-")
    year = int(second[0])
    month = int(second[1])
    day = int(second[2])
    return year, month, day


def number_days(year,month,day):
    """
    return the number of days between the date and 0 BC
    """
    monthdays = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    return year * 365 + monthdays[month-1] + day


def days_uploaded(year, month, day, current_year, current_month, current_date):
    """
    calculate the number of days between two dates
    """
    return number_days(current_year, current_month, current_date) - number_days(year,month,day)



###################################################################################
# Webscraping
###################################################################################


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def get_views(url):
    """
    Input: url of a youtube channel
    Output: the number of views on that channel currently
    """
    try:
        page = requests.get(url)
        youtube = html.fromstring(page.text)
        video_count = youtube.xpath("//*[(@class='watch-view-count')]/text()")
        views = str(video_count[0]).split(" ")[0]
        return float(str(video_count[0]).split(" ")[0].replace(',',''))

    except:
        log_error("this url no longer exists")
        return 0


###################################################################################
# Generate CSV
###################################################################################


def make_dictionary(doc,n):
    """
    opens a csv file containing data on trending youtube videos
    goes through each url in the file and find the number of videos it has now
    then return
    """
    old_data = csv.reader(open(doc))

    vid_dict = {}
    count = 0
    for list in old_data:
        if count != 0 and count < n:
            new_views = get_views("https://www.youtube.com/watch?v=" + list[0])
            if new_views != 0:

                x, y, z = stringtoint(list[1:][4])
                publishing_time = days_uploaded(x, y, z, 2018, 12, 14)
                views = float(list[1:][6])
                likes = float(list[1:][7])
                dislikes = float(list[1:][8])
                comment_count = float(list[1:][9])
                views_change = new_views - views

                vid_dict[list[0]] = [publishing_time, views, likes, dislikes, comment_count, new_views, views_change]
        print count
        count += 1
    return vid_dict


def make_csv(vid_dict):
    """
    return a csv from a dictionary mapping the video url of a youtube video to its
    publish time, views, likes, dislikes, commend count and the new number of views
    """
    csv_file = open('test_run.csv', 'w')
    writer = csv.writer(csv_file)
    writer.writerow(
        ["video_id", "publish_time", "views", "likes", "dislikes", "comment_count", "new_views", "views_change"])
    for key, value in vid_dict.items():
        value.insert(0, key)
        writer.writerow(value)

    csv_file.close()


def test():
    make_csv(make_dictionary("USvideos.csv", 200))


def main():
    make_csv(make_dictionary("USvideos.csv", 40000))

main()



