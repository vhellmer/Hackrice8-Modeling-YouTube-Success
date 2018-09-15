import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("combined.csv")

def plot(x,y,xlabel,ylabel):
    plt.scatter(x, y, 1, "green")
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

plot(data['x'], data['y'],'likes','views_change')
#lot(data['likes'], data['views_change'],'likes','views_change')