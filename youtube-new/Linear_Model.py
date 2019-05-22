import statsmodels.api as sm
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn import linear_model as lm

def linear_model(y,x):
    """

    generate a linear model from datasets x and y
    """
    return sm.OLS(y, x).fit()

def correlation_map(data):
    """
    plot the correlation heat mapping of a dataset
    """
    corr = data.corr()
    sns.heatmap(corr,
                xticklabels=corr.columns.values,
                yticklabels=corr.columns.values)
    plt.show()

def pair_plot(data_set):
    """
    plot relation between each variable
    """
    sns.pairplot(data_set[["new_views", "views", "likes", "dislikes", "comment_count"]], diag_kind="kde")
    plt.show()

# data = pd.read_csv("Results.csv")
# y = np.log1p(data.new_views)
# x = pd.concat(
#     [np.log1p(data.views),
#      np.log1p(data.likes),
#      np.log1p(data.dislikes),
#      np.log1p(data.comment_count)],axis=1)
# model = linear_model(y,x)
# correlation_map(x)

raw_data = pd.read_csv("Results.csv")

dataset = pd.concat(
    [np.log1p(raw_data.new_views),
     np.log1p(raw_data.views),
     np.log1p(raw_data.likes),
     np.log1p(raw_data.dislikes),
     np.log1p(raw_data.comment_count)],axis=1)

train_dataset = dataset.sample(frac=0.8,random_state=0)
test_dataset = dataset.drop(train_dataset.index)
train_labels = train_dataset.pop('new_views')
test_labels = test_dataset.pop('new_views')

pair_plot(dataset)
model = linear_model(train_labels,train_dataset)
print model.summary()




