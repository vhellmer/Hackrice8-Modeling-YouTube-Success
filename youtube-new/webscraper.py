import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from collections import defaultdict

# List that contains all url id information from videos
url_list = []
with open('USvideos.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        url_list.append(row[0])
url_list = url_list[1:]


# Opens chrome (MUST have selenium plugin in PATH or will cause an error)
driver = webdriver.Chrome()

# Default dict of type list that will contain key of vid_id and value of array views, likes, dislikes, comment_count
vid_dict = defaultdict(list)

# Goes through a section of urls in list
for i in range(25000, 35000, 20):

    url = url_list[i]
    vid_dict[url] = []

    # Tries to get link, or continues if fails
    try:
        driver.get("https://www.youtube.com/watch?v=" + url)
    except:
        print("website failed to load")
        vid_dict[url].append(str(0))
        vid_dict[url].append(str(0))
        vid_dict[url].append(str(0))
        vid_dict[url].append(str(0))
        continue

    # Tries to get views, fails if video is taken down
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="count"]/yt-view-count-renderer/span[1]'))
        wait(driver, 3).until(element_present)
        views = driver.find_element_by_xpath('//*[@id="count"]/yt-view-count-renderer/span[1]').text
        vid_dict[url].append(str(views).split(" ")[0])
    except:
        print("views failed: ", url)
        vid_dict[url].append(str(0))
        vid_dict[url].append(str(0))
        vid_dict[url].append(str(0))
        vid_dict[url].append(str(0))
        continue

    # # Tries to get likes
    # try:
    #     element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a'))
    #     wait(driver, 5).until(element_present)
    #     likes = driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a').find_element_by_id("text").get_attribute("aria-label")
    #     vid_dict[url].append(str(likes).split(" ")[0])
    # except:
    #     print("likes failed: ", url)
    #     vid_dict[url].append(str(0))
    #
    # # Tries to get dislikes
    # try:
    #     element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[2]/a'))
    #     wait(driver, 5).until(element_present)
    #     dislikes = driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[2]/a').find_element_by_id("text").get_attribute("aria-label")
    #     vid_dict[url].append(str(dislikes).split(" ")[0])
    # except:
    #     print("dislikes failed: ", url)
    #     vid_dict[url].append(str(0))
    #
    # # Tries to get comment_count, may fail if comments are disabled
    # try:
    #     element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="count"]/yt-formatted-string'))
    #     wait(driver, 5).until(element_present)
    #     comments = driver.find_element_by_xpath('//*[@id="count"]/yt-formatted-string').text
    #     vid_dict[url].append(str(comments).split(" ")[0])
    # except:
    #     print("comments failed: ", url)
    #     vid_dict[url].append(str(0))

# Appends to existing csv file
csv_file = open('new_vid_data2.csv', 'a')
writer = csv.writer(csv_file)

#Add following line for header if making a new file:
#writer.writerow(["video id", "views"])

for key, value in vid_dict.items():
    value.insert(0, key)
    writer.writerow(value)

csv_file.close()
driver.close()
