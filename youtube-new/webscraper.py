import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from time import sleep

url_list = []
with open('USvideos.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        url_list.append(row[0])


# Opens chrome (MUST have selenium plugin in PATH or will cause an error)
driver = webdriver.Chrome()

# File for strains to be written to
# new_file = open("current_video_data.csv", "w")
url_list = url_list[1:]
for url in url_list:
    driver.get("https://www.youtube.com/watch?v=" + url)
    sleep(2)
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="count"]/yt-view-count-renderer/span[1]'))
        wait(driver, 5).until(element_present)
        views = driver.find_element_by_xpath('//*[@id="count"]/yt-view-count-renderer/span[1]').text
        print(views)
    except:
       print("views failed: ", url)

    sleep(3)
    likes = driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a').text
    print(likes)
    #print("likes failed: ", url)
    #try:
        #dislikes = driver.find_element_by_xpath('//*[@id="text"]').text
        #print(dislikes)
    #except:
        #print("dislikes failed: ", url)
    try:
        comments = driver.find_element_by_xpath('//*[@id="count"]/yt-formatted-string').text
        print(comments)
    except:
        print("comments failed: ", url)

driver.close()
