# Classification

1. Load the `swiss` data set with `pydataset.data`
1. Transform the `Catholic` variable into a categorical variable named
   `is_catholic`. The values should be either `Catholic` or `Not Catholic`.
1. Drop the `Catholic` column.
1. Split the data into training and test data sets. We will be trying to predict
   whether or not a province is catholic.
1. Fit a decision tree classifier using the `Education` and `Fertility`
   features. Measure the model's performance using accuracy, precision, and
   recall.
1. Fit a logistic regression model using `Agriculture` and `Examination`.
   Measure the model's performance.
1. Fit a K Nearest Neighbors model using two features of your choice. Measure
   the model's performance.
1. Use the best model from the ones above on your test data set and evaluate the
   model's predictions.
1. Explain how/why your model is making the predictions that it is.
