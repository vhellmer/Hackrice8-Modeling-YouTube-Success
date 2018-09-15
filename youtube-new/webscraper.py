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

for url in url_list:
    driver.get("https://www.youtube.com/watch?v=" + url)
    sleep(5)

driver.close()
