import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import Generate_csv
from wordcloud import WordCloud, STOPWORDS

data = pd.read_csv("combined2.csv")

def plot(x,y,xlabel,ylabel):
    plt.scatter(x, y, 1, "blue")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def remove_outliers(x,n):
    if x > n:
        return n
    else:
        return x


#data['x'] = data['likes'].apply(lambda x: remove_outliers(x,300000))
#data['y'] = data['views_change'].apply(lambda x: remove_outliers(x, 5000000))
data['x'] = np.log(data['comment_count'] + 1)
data['y'] = np.log(data['views_change'] + 1)
#data['%change'] = data['views_change'] / data['views']

plot(data['x'], data['y'],'comment_count','views_change')
plot(data['x'], data['y'],'comment_count','views_change')

