# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 11:32:30 2018

@author: DELL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def readfile(csvfile):
    df = pd.read_csv(csvfile)
    return df["likes"], df["dislikes"], df["publish_time"], df["views_change"]

likes = readfile("combined2.csv")[0]
dislikes = readfile("combined2.csv")[1]
pub = readfile("combined2.csv")[2]    
change = readfile("combined2.csv")[3]    

print (pub[:90])
"""
Change three integers representing the date uploaded to the no. of days the video has 
has been uploaded for
"""
def stringtoint(stringdate):
    first = stringdate.split("T")[0]
    second = first.split("-")
    year = int(second[0])
    month = int(second[1])
    day = int(second[2])
    return year, month, day

def monthday_array():
    """
    helper function for days_uploaded
    """
    monthday = [31,0]
    for i in range(7,0,-1):
        if i % 2 == 1:
            monthday.insert(0,monthday[0] + 31)
        elif i == 2:
            monthday.insert(0,monthday[0] + 28)
        else:
            monthday.insert(0,monthday[0] + 30)
    for i in range(9,12):
        if i == 11:
            monthday.append(monthday[-1] - 31)
        else:
            monthday.append(monthday[-1] - 30)
    monthday.insert(0,0)
    return monthday

monthday = monthday_array()

def days_uploaded(year, month, day):
    # assuming each year has 365 days
    days = (2018 - year) * 365
      
    days += monthday[month]
    
    days += 15 - day
    
    return days

time = []
for i in pub:
    ymd = stringtoint(i)  
    pyear = ymd[0]
    pmonth = ymd[1]
    pday = ymd[2]
    time.append(days_uploaded(pyear,pmonth,pday))
    
print (time[0:29])
        
"""
x,y,z are three arrays of values for our x-var, y-var; x and y will be plotted
on their respective axis, while z-var will be represented by the size of the
dot on our scatterplot.
"""
# =============================================================================
# Graphing functions
# =============================================================================

def scattercompare2(x,y, labelx, labely):

    plt.scatter( x,y, s =1, c = 'red')
    plt.xlabel(labelx)
    plt.ylabel(labely)
#    ax = plt.gca()
#    ax.set_xlim([0,3000])
#    ax.set_ylim([0,30000])
    plt.show()
    
print (len(likes), len(change))
scattercompare2(likes, change, "no. of likes", "change in viewership")

scattercompare2(dislikes, change, "no. of dislikes", "change in viewership")

scattercompare2(time, change, "time since upload", "change in viewership")

# =============================================================================
# Curve fitting and R square calculating Function for y vs x
# =============================================================================

def lin_func(x, a, b):
    return  a * x + b


def inv_func(x, k, b):
    return k /x + b

#def inv_2_func(x, k ,b):
#    return k/(x**2) + b

def fit_curve(x_data, y_data, func):
    params, params_covariance = optimize.curve_fit(func, x_data, y_data)
    return params

def plot_curve(x_data, y_data, func):
    plt.scatter(x_data, y_data, label='Data')
    plt.plot(x_data, func(x_data, fit_curve(x_data, y_data, func)[0], 
                          fit_curve(x_data, y_data, func)[1]))
    plt.show()
    
plot_curve(likes, change, lin_func)
plot_curve(dislikes, change, lin_func)
#plot_curve(time, change, lin_func)
# =============================================================================
# Create a multiple linear regression model from, hopefully, all independent 
# variables, y^ = ax1 + bx2 + cx3 + d, to predict Y, change in viewership
# =============================================================================

from sklearn import linear_model

def combine_var(lst1, lst2, lst3):
    lst = []
    lst.append(list(lst1))
    lst.append(list(lst2))
    lst.append(list(lst3))
    return lst


combine = combine_var(likes, dislikes, time)

import statsmodels.api as sm # import statsmodels 

 #X usually means our input variables (or independent variables)
y = change ## Y usually means our output/dependent variable
 ## let's add an intercept (beta_0) to our model

# Note the difference in argument order
model = sm.OLS([1,2,3], [[1,2],[3,2],[3,2]]).fit() ## sm.OLS(output, input)
predictions = model.predict([[1,2],[3,2],[3,2]])

# Print out the statistics
print (model.summary())
    
def graph_predict_actual(pred_array, act_array):
    plt.scatter(range(len(pred_array)), pred_array, color = "red", label = "predicted")
    plt.scatter(range(len(act_array)), act_array, color = "blue", label = "actual")
    plt.xlabel = "index of youtube videos"
    plt.ylabel = "change in viewership"
    plt.show()

# =============================================================================
#print (mult_reg_model_predi(likes, dislikes, time, change))
print (len(change))
print (type(likes))
    