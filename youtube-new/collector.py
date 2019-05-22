"""
    @Description:   This python collects data from YouTube Videos
    @               such as views, likes, dislikes, etc
    @
    @Author:        Ken Zeng
"""

import requests
from lxml import html
import csv
from datetime import datetime
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from contextlib import closing
import csv
from collections import defaultdict


class Collector(object):
    """
    A collector that takes a list of url as an input
    and scrapes data from those urls
    """
    def __init__(self, url_list):

        self.url_list = url_list
        self.valid_urls = set([])

        # each dictionary maps url to the information on each url
        self.info = {}

        # set of urls that disabled one of the above
        # but what should I do with all the disabled channels?
        self.disabled = set([])

    def get_info(self):
        """
        return a dictionary mapping each url to
        all the information collected on the url
        """
        return self.info

    def get_disabled(self):
        """
        get a list of all YouTube videos that disabled views
        """
        return self.disabled

    def get_valid(self):
        """
        return a list of all valid urls
        """
        return self.valid_urls

    def collect(self):
        """
        collects views, likes, dislikes of a youtube video
        It can then save the results as a csv
        """
        print("start collection...")

        for i in range(len(self.url_list)):
            # sets a check point every time 500 websites are visited
            print(i)
            if i % 10 == 0 and i != 0:
                print("visited  " + str(i) + " urls")
            url = url_list[i]
            # check if the url is a site on YouTube
            if url[:29] != "https://www.youtube.com/watch":
                pass
            try:
                page = requests.get(url)
                youtube = html.fromstring(page.text)
                self.info[url] = {}

                try:  # try to get title
                    title = youtube.xpath("//*[(@class='watch-title')]/text()")
                    self.info[url]["title"] = str(title[0])
                except:
                    self.disabled.append(url)
                try:  # try to get date
                    title = youtube.xpath("//*[(@class='watch-time-text')]/text()")
                    self.info[url]["date"] = str(title[0])
                except:
                    self.disabled.append(url)
                try:  # try to get views
                    view_count = youtube.xpath("//*[(@class='watch-view-count')]/text()")
                    self.info[url]["views"] = float(str(view_count[0]).split(" ")[0].replace(',', ''))
                except:
                    self.disabled.append(url)

                # Todo: get correct xpaths to likes and dislikes
                # try:  # try to get likes
                #     like_counts = youtube.xpath("//*[(@class='like-button-renderer-like-button')]/text()")
                #     self.info[url]["likes"] = float(str(like_counts[0]).split(" ")[0].replace(',', ''))
                # except:
                #     disabled.append(url)
                # try:  # try to get dislikes
                #     dislike_counts = youtube.xpath("//*[(@class='like-button-renderer-dislike-button')]/text()")
                #     self.info[url]["dislikes"] = float(str(dislike_counts[0]).split(" ")[0].replace(',', ''))
                # except:
                #     disabled.append(url)

                self.valid_url.append(url)
            except:
                pass

        print("Collection finished.")

    def save(self, file_name):
        """
                save the file as a csv file
                """

        csv_file = open(file_name, 'w')
        writer = csv.writer(csv_file)
        row_titles = ["url", "title", "date", "views"]
        writer.writerow(row_titles)

        # generate rest of the csv
        for url in self.valid_urls:
            if url not in self.disabled:
                value = [url] + [self.info[url][name] for name in row_titles[1:]]
                writer.writerow(value)
        csv_file.close()

        print("File saved")



if __name__ == "__main__":

    url = "https://www.youtube.com/watch?v=87yupacw8Jc&t=3592s"
    url1 = "https://www.youtube.com/watch?v=1QCK_gFGi90"
    url_list = [url,url1]
    web_scraper = Collector(url_list)
    web_scraper.collect()
    print(web_scraper.get_info())
    web_scraper.save("results.csv")