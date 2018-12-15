# hackrice8: Modeling YouTube Success
Contains youtube analytic scripts and files
Using multiple variables from each youtube video to predict the change in views over time.
Y ˆ = A + B1(X1) + B2(X2) + B3(X3) + B4(X4)
Find R squared of Y^(predicted change in view) compared to Y(the actual change in views)
Varible:
Y = change in views from the date the data on Kaggle was collected to today, Sep 15th
Y = current no. of views - past no. of views
X1 = likes; X2 = dislikes; X3 = time elapsed since the video was uploaded

Separate data into 70% training/30% testing

1. Retrieve data for just the current views from the same youtube videos 
using the links provided in the youtube analytic scripts from Kaggle.

2. Separate the dataset into training data and testing data(70%,30%).

(Use day_calc function to change from the year-month-day format to no of days passed)
3. An array for:
Training likes, Training dislikes,training times, training current views, training past views
testing likes, testing dislikes,testing times, testing current views, testing past views

4. Construct new array by:
training change = subtracting training current by training past
testing change = subtracting testing current by testing past

5. Do scatterplot for:
Training change vs training likes; vs training dislikes; vs no. of days since upload
Determine if a linear relationship
Try doing various curves to visualize and model the relationship

6. Run linear regression on three variables with the actual change in views, get a,b,c params
Construct an array of predicted change in views based on the three variables in the test_data and our model a,b,c

7. Graphing, predicted curve for each corresponding videos, with an index assigned to each video as the x-axis
compare the predicted change in view with the actual for each x(index)
Calculate R square for our curve and the actual change in view in the test_data.



