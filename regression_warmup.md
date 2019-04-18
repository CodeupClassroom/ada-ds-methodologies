# Warmup

Create a notebook or python script named `regression_warmup` for this exercise.

0. Make sure you have the `pydataset` library installed.

    ```
    python -m pip install --upgrade pydataset
    ```

1. Load the swiss data set

    ```python
    from pydataset import data

    data('swiss')
    ```

    Skim through the documentation for the dataset

    ```python
    data('swiss', show_doc=True)
    ```

    We'll be using `Fertility` as our target variable to predict.

1. Briefly take a look at the data. You won't need to do any cleaning or
   preparation, but you should get an overview of the data. Visualize the
   distribution of each variable, and take a look at how the individual features
   correlate with the target variable.

1. Split the data into training and test data sets.

1. Fit a linear model using `Agriculture` and `Catholic` as the independent
   variables. Measure the model's performance.

1. Fit a linear model using `Education` and `Examination`. Measure the model's
   performance.

1. Use the best of the above two models and measure that model's performance on
   the test set.

1. Fit a linear model using all of the independent variables. Take a look at the
   resulting model's coefficients. What do these tell us? How do we interpret
   them?
