import pandas as pd
import statsmodels.formula.api as sm
import numpy as np

ken = pd.read_csv("combined2.csv")
ken["logviews"] = ken["views_change"].apply(np.log1p)
ken["loglikes"] = ken["likes"].apply(np.log1p)
ken["logdislikes"] = ken["dislikes"].apply(np.log1p)
ken["logcomment_count"] = ken["comment_count"].apply(np.log1p)
# ken["lratio"] = ken["likes"] / (ken["dislikes"] + ken["likes"])


ken2 = pd.read_csv("combined4.csv")
ken2.columns
ken2["logviews_change"] = ken2["views_change"].apply(np.log1p)
ken2["logtime"] = ken2["publish_time"].apply(np.log1p)
ken2["logcomments"] = ken2["comment_count"].apply(np.log1p)
ken2["loglikes"] = ken2["likes"].apply(np.log1p)
ken2["timelikes"] = ken2["publish_time"] * ken2["likes"]
ken2["logtimelikes"] = ken2["timelikes"].apply(np.log1p)

#result = sm.ols(formula="logviews_change ~ logtimelikes + logtime + logcomments", data=ken2).fit()
#ken2.plot.scatter(x = "logviews_change", y = "logtimelikes")

#print(result.summary())
#print(result.params)

#result = sm.ols(formula="logviews ~ loglikes + logdislikes + logcomment_count", data=ken).fit()
# result = sm.ols(formula="views_change ~ likes + dislikes + comment_count", data=ken).fit()
#ken.plot.scatter(x = "logviews", y = "loglikes", )
#print(result.summary())
#print(result.params)

result = sm.ols(formula= "logviews_change ~ loglikes", data=ken2).fit()
print(result.summary())
#print(result.params)

#"logviews_change ~ loglikes":  R-squared: 0.659,