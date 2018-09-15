import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#import os
#from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS

df_yout = pd.read_csv("USvideos.csv")

#Looking some information of the data
#print(df_yout)
#print(df_yout.shape)
#print(df_yout.nunique())


#Looking at each column
#print(df_yout['views'])
#print(df_yout['likes'])
#print(df_yout['dislikes'])
#print(df_yout['comment_count'])


#log the results
df_yout['likes_log'] = np.log(df_yout['likes'] + 1)
df_yout['views_log'] = np.log(df_yout['views'] + 1)
df_yout['dislikes_log'] = np.log(df_yout['dislikes'] + 1)
df_yout['comment_log'] = np.log(df_yout['comment_count'] + 1)

#convert number to its catergory name
df_yout['category_name'] = np.nan
df_yout.loc[(df_yout["category_id"] == 1),"category_name"] = 'Film and Animation'
df_yout.loc[(df_yout["category_id"] == 2),"category_name"] = 'Cars and Vehicles'
df_yout.loc[(df_yout["category_id"] == 10),"category_name"] = 'Music'
df_yout.loc[(df_yout["category_id"] == 15),"category_name"] = 'Pets and Animals'
df_yout.loc[(df_yout["category_id"] == 17),"category_name"] = 'Sport'
df_yout.loc[(df_yout["category_id"] == 19),"category_name"] = 'Travel and Events'
df_yout.loc[(df_yout["category_id"] == 20),"category_name"] = 'Gaming'
df_yout.loc[(df_yout["category_id"] == 22),"category_name"] = 'People and Blogs'
df_yout.loc[(df_yout["category_id"] == 23),"category_name"] = 'Comedy'
df_yout.loc[(df_yout["category_id"] == 24),"category_name"] = 'Entertainment'
df_yout.loc[(df_yout["category_id"] == 25),"category_name"] = 'News and Politics'
df_yout.loc[(df_yout["category_id"] == 26),"category_name"] = 'How to and Style'
df_yout.loc[(df_yout["category_id"] == 27),"category_name"] = 'Education'
df_yout.loc[(df_yout["category_id"] == 28),"category_name"] = 'Science and Technology'
df_yout.loc[(df_yout["category_id"] == 29),"category_name"] = 'Non Profits and Activism'
df_yout.loc[(df_yout["category_id"] == 25),"category_name"] = 'News & Politics'

#Looking at each column
#print(df_yout['views'])
#print(df_yout['likes'])
#print(df_yout['dislikes'])
#print(df_yout['comment_count'])
#
df_yout['like_rate'] =  df_yout ['likes'] / df_yout['views'] * 100
df_yout['dislike_rate'] =  df_yout ['dislikes'] / df_yout['views'] * 100
df_yout['comment_rate'] =  df_yout ['comment_count'] / df_yout['views'] * 100

df_yout['like_to_dislike'] =  df_yout ['likes'] / df_yout['dislikes']
#print(df_yout['like_to_dislike'])

df_yout['area'] = df_yout['views'] / 100000

def convert_to_list(input):
    output = []
    for item in input:
        output += [item]
    return output

#plt.scatter(convert_to_list(df_yout['likes_log']),convert_to_list(df_yout['dislikes_log']),convert_to_list(df_yout['area']),"blue",alpha = 0.1)
plt.scatter(df_yout['views'],df_yout['like_to_dislike'],1,"green")
plt.show()
