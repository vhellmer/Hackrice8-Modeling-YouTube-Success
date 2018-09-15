# row 0 = url tag
# row 1 = yr, day, month trending
# row 2 = video title
# row 3 = channel name
# row 4 = video category (i.e. history, comedy)
# row 5 = detailed date posted
# row 6 = tags
# row 7 = views
# row 8 = likes
# row 9 = dislikes
# row 10 = comment count
# row 11 = thumbnail link
# row 12, 13, 14 = booleans comments_disabled, ratings_disabled, video_error_or_removed
# row 15 = description

import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

file = pd.read_csv("USvideos.csv")

# Looking some information of the data
print(file.sort_values(['views']))
print(file.shape)
print(file.nunique())

file['like_rate'] = file['likes'] / file['views'] * 100
file['dislike_rate'] = file['dislikes'] / file['views'] * 100
file['comment_rate'] = file['comment_count'] / file['views'] * 100

print(file['dislike_rate'])
