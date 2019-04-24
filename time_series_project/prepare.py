# # Data Preparation
#
# 0. Planning
# 1. Data Acquisition
# 2. **Data Preparation** <- You are here
# 3. Data Exploration
# 4. Data Modeling
#
# This script defines functions that perform a handful of data wrangling
# operations on the fitbit data:
#
# ## Overview
#
# - The column names have spaces in them, we'll make them more consistent.
# - Some of the numeric columns are formatted such that they have a comma in
#   them. While this might be nice for human readers, we'll need to handle this
#   data such that we represent it with a numeric type.
# - Properly convert all the date columns to date data types.
# - The activity data frame has seperate columns for different intensities of
#   active minutes we will just combine this into one measure for total active
#   minutes.
#
# In addition, we'll add the different components of the date to each row.
import pandas as pd
from typing import Tuple
from datetime import datetime

#
# ## Implementation
#

def log(msg):
    print(f'[{datetime.now()} prepare.py] {msg}')

def handle_commas(s: pd.Series) -> pd.Series:
    'Given a Series, removes any commas and casts the series to an int type.'
    return s.str.replace(',', '').astype(int)

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    'Lowercases and replaces spaces with underscores in column names'
    df.columns = [col.lower().replace(' ', '_') for col in df]
    return df

def prep_food_data(df: pd.DataFrame) -> pd.DataFrame:
    log('Prepping food data frame')
    clean_column_names(df)
    df.date = pd.to_datetime(df.date)
    df.calories_in = handle_commas(df.calories_in)
    return df.sort_values(by='date')

def prep_activity_data(df: pd.DataFrame) -> pd.DataFrame:
    log('Prepping activity data frame')
    clean_column_names(df)
    df.date = pd.to_datetime(df.date)

    # Columns that should actually be numbers, but that could have commas in
    # them, so pandas treats them as objects (strings)
    number_cols = ['calories_burned', 'steps', 'minutes_sedentary',
                   'minutes_lightly_active', 'minutes_fairly_active',
                   'minutes_very_active', 'activity_calories']
    # We'll `select_dtypes` here so that if a column is already numeric, we
    # won't try to re-process it.
    for col in df[number_cols].select_dtypes('object'):
        df[col] = handle_commas(df[col])

    # We'll do a little bit of feature engineering here and combine the seperate
    # active minutes columns into a single column reprepseting overall active
    # minutes.
    df['minutes_active'] = (df.minutes_lightly_active +
                            df.minutes_fairly_active +
                            df.minutes_very_active)
    df.drop(
        ['minutes_lightly_active', 'minutes_fairly_active', 'minutes_very_active'],
        axis=1, inplace=True)

    df['month'] = df.date.dt.strftime('%m-%b')
    df['weekday'] = df.date.dt.day_name().str[:3]

    return df.sort_values(by='date')

def prep_fitbit_data(data: Tuple[pd.DataFrame, pd.DataFrame]) -> Tuple[pd.DataFrame, pd.DataFrame]:
    foods, activity = data
    return prep_food_data(foods), prep_activity_data(activity)

# For testing we will add some code that only runs when we invoke the file
# directly, e.g.
#
# ```
# python -i prepare.py
# ```
#
# to test out our preparation functions and play with the resulting data frames.
if __name__ == '__main__':
    from acquire import get_fitbit_data
    foods, activity = get_fitbit_data()

    foods = prep_food_data(foods)
    activity = prep_activity_data(activity)
