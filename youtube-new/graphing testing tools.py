# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 11:32:30 2018

@author: DELL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind


"""
x,y,z are three arrays of values for our x-var, y-var; x and y will be plotted
on their respective axis, while z-var will be represented by the size of the
dot on our scatterplot.
"""

def scattercompare2(x,y, labelx, labely):

    plt.scatter(x,y, s = areaz, c = 'red', alpha = 0.7)
    plt.xlabel = (labelx)
    plt.ylabel = (labely)
    plt.show()
    
def scattercompare3(x,y,z,labelx, labely):
    
    areaz = (1000 * z)
    plt.scatter(x,y, s = areaz, c = 'red', alpha = 0.7)
    plt.xlabel = (labelx)
    plt.ylabel = (labely)

def t-testing(x,y):
    t, p = ttest_ind(normal,tumor)
    return t


    