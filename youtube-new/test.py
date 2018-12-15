import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import Generate_csv
from wordcloud import WordCloud, STOPWORDS

data = pd.read_csv("Results.csv")

def plot(x,y,xlabel,ylabel):
    """
    plot the graph y vs x
    """
    plt.scatter(x, y, 1, "green")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def log1p_plot(data,xlabel,ylabel):
    """

    :param data:
    :param xlabel:
    :param ylabel:
    :return:
    """
    plot(np.log(data[xlabel] + 1), np.log(data[ylabel] + 1),xlabel, ylabel)

def normal_plot(data,xlabel, ylabel):
    """

    :param data:
    :param xlabel:
    :param ylabel:
    :return:
    """
    plot(data[xlabel],data[ylabel], xlabel, ylabel)


#data['x'] = data['likes'].apply(lambda x: remove_outliers(x,300000))
#data['y'] = data['views_change'].apply(lambda x: remove_outliers(x, 5000000))
#data['x'] = np.log(data['publish_time'] + 1)
#data['y'] = np.log(data['views_change'] + 1)
#data['%change'] = data['views_change'] / data['views']

#plot(data['publish_time'], data['y'],'publish_time','views_change')
#plot(data['x'], data['y'],'comment_count','views_change')

log1p_plot(data,'publish_time','views_change')
normal_plot(data,'publish_time','views_change')
