# More Exercises

1. Use spark to read in the necessary information from the `employees` database
   to answer these questions:

    - How many employees currently work in each department?
    - What is the average salary by title of employees in the Finance
      department?  Include only current salaries and only employees currently
      working in Finance.
    - How many senior engineers are there in each department? Include only
      current titles and only employees currently working in each department.
    - Calculate the range (i.e. max - min) of the salaries for each department.
      Include only current salaries and employees currently working in each
      department.
    - Is the average salary increasing over time?
    - Which department has the biggest shift in average salary over time?

1. Load the `mpg` dataset as a spark data frame.

    ```python
    mpg = spark.createDataFrame(data('mpg'))
    ```

    - Create a new column named `average_mileage` that is the average of the
      city and highway mileage.
    - What is the distribution of vehicle class across manufacturers?
    - What is the average highway mileage for each class of vehicle?
    - Do vehicles with front-wheel or rear-wheel drive have a higher minimum
      city mileage?
    - What is the distribution of transmission type across manufacturer?
    - Do vehicles with a automatic transmission or manual transmission have a
      higher average mileage? Is this difference statistically significant?

    Create a model that preedicts `average_mileage` based on the other features.

1. Load the `Mammals` dataset as a spark data frame. Read the documentation for
   it, and answer the following questions:

    - How many rows and columns are there?
    - What are the data types?
    - What is the the weight of the fastest animal?
    - What is the overal percentage of specials?
    - How many animals are hoppers that are above the median speed? What
      percentage is this?
