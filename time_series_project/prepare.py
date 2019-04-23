# # Data Preparation
#
# This script defines functions that perform a handful of data wrangling
# operations on the fitbit data:
#
# - The column names have spaces in them, we'll make them more consistent.
# - Some of the numeric columns are formatted such that they have a comma in
#   them. While this might be nice for human readers, we'll need to handle this
#   data such that we represent it with a numeric type.
# - Properly convert all the date columns to date data types.
# - The activity data frame has seperate columns for different intensities of
#   active minutes we will just combine this into one measure for total active
#   minutes.
import pandas as pd

def handle_commas(s: pd.Series) -> pd.Series:
    'Given a Series, removes any commas and casts the series to an int type.'
    return s.str.replace(',', '').astype(int)

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    'Lowercases and replaces spaces with underscores in column names'
    df.columns = [col.lower().replace(' ', '_') for col in df]
    return df

def prep_food_data(df: pd.DataFrame) -> pd.DataFrame:
    clean_column_names(df)
    df.date = pd.to_datetime(df.date)
    df.calories_in = handle_commas(df.calories_in)

def prep_activity_data(df: pd.DataFrame) -> pd.DataFrame:
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
        print('Processing ' + col)
        df[col] = handle_commas(df[col])

    # Combine the seperate active minutes columns into a single column
    # reprepseting overall active minutes.
    df['minutes_active'] = (df.minutes_lightly_active +
                            df.minutes_fairly_active +
                            df.minutes_very_active)

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
