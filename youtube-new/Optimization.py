import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
#INPUT ken2

def subsets(input):
    if not input:
        return [[]]
    else:
        children = subsets(input[1:])
        childrenPlus = [[input[0]] + x for x in children]
        return children + childrenPlus


ken2 = pd.read_csv("combined5.csv")
column_list = list(ken2.columns)
for columns in column_list:
     ken2[columns] = ken2[columns].apply(np.log1p)


column_list = column_list[1:]
head_power_set = subsets(column_list)

head_power_set = head_power_set[1:]

maxr = 0
maxcombo = None
count = 1.0
total = len(head_power_set)
for combos in head_power_set:
    print(count / total)
    count += 1
    formula_string = "views_change ~ "
    if combos:
        for header_index in range(len(combos)):
            if header_index == 0:
                formula_string += combos[0]
            else:
                formula_string = formula_string + " + " + combos[header_index]
        # print(formula_string)
        result = sm.ols(formula= formula_string, data=ken2).fit()

        if result.rsquared > maxr:
            maxr = result.rsquared
            maxcombo = result

print(maxr)
print(maxcombo.summary())
