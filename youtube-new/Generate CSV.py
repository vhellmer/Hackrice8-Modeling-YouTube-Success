import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from collections import defaultdict

def new_cvs(original_stats, new_stats):

    new_data = csv.reader(open(new_stats))
    old_data = csv.reader(open(original_stats))

    print(new_data)

    url_list = []
    new_url_dict = {}
    count1 = 0
    for list in new_data:
        if count1 != 0:
            url_list += [list[0]]
            new_url_dict[list[0]] = [float(list[1].replace(',',''))]
        count1 += 1

    url_dict = {}
    count2 = 0
    for list in old_data:
        if count2 != 0:
            url_dict[list[0]] = list[1:]
        count2 += 1

    vid_dict = {}
    for url in url_list:
        if url in url_dict:
            # publish time, views, likes, dislikes, comment_count
            vid_dict[url] = [url_dict[url][4], float(url_dict[url][6]), float(url_dict[url][7]), float(url_dict[url][8]), float(url_dict[url][9])] + new_url_dict[url]

    csv_file = open('combined.csv', 'w')
    writer = csv.writer(csv_file)
    writer.writerow(["video_id", "publish_time","views", "likes", "dislikes", "comment_count","new_views"])
    for key, value in vid_dict.items():
        value.insert(0, key)
        writer.writerow(value)

    csv_file.close()

new_cvs("USvideos.csv", "new_results.csv")