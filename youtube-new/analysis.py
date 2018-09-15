import pandas as pd
import numpy as np

df_yout = pd.read_csv("USvideos.csv")

#Looking some information of the data
print(df_yout.shape)
print(df_yout.nunique())