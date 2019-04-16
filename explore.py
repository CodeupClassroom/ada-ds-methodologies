# 1. Write a function that will take, as input, a dataframe and a list containing the column names of all ordered numeric variables. It will output a pairplot and a heatmap.
# 2. Write 2+ other functions for plotting in plots that will contribute to your exploration of what is driving the logerror.  Some ideas: 
#    - seaborn's relplot where you can use 4 dimensions: x & y are continuous or continuous-like, color is discrete with limited number of values, size is numeric & ordered. 
#    - seaborn's swarmplot (x, y, color)
#    - logerror is normally distributed, so it is a great opportunity to use the t-test to test for significant differences in the logerror by creating sample groups based on various variables.  e.g. Is logerror significantly different for properties in Los Angeles County vs Orange County (or Ventura County)?  Is logerror significantly different for properties that are delinquent on their taxes vs those that are not?  Is logerror significantly different for properties built prior to 1960 than those built later than 2000?
# 4. Chi-Squared test:  run at least one at least 1 $\chi^{2}$ test and summarize conclusions.  Ideas: If you split logerror into quartiles, you can expect the overall probability of falling into a single quartile to be 25%.  Now, add another variable, like bedrooms (and you can bin these if you want fewer distinct values) and compare the probabilities of bedrooms with logerror quartiles.  See the example in the Classification_Project notebook we reviewed on how to implement chi-squared.
# 5. write a function that will take a dataframe and a list of continuous-like column names to plot each combination of variables in the chart type of your choice.
# 6. Write a function that will take a dataframe and a list of continuous-like column names, limited discrete/categorical column names (<10), and names of columns with limited discrete/categorical values that could be used as color/hue (<5 or so).  It will plot each combination of variables in the chart type of your choice (that takes those types and number of dimensions) 

import seaborn as sns
import matplotlib.pyplot as plt

def pair_plot(df):
    p = sns.pairplot(df)
    return p

def heat_map(df):
    plt.figure(figsize=(8,6))
    q = sns.heatmap(df.corr(), cmap='RdYlBu', annot=True, center=0)
    return q