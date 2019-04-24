# # Making Predictions
#
# This script will use the best model that came out of the modeling process (see
# the modeling notebook for more details on this) to make predictions for the
# next two weeks of data.

import pandas as pd
from fbprophet import Prophet

from acquire import get_fitbit_data
from prepare import prep_fitbit_data

# All of the values we are trying to predict
TARGETS = [
    'calories_burned',
    'distance',
    'steps',
    'floors',
    'minutes_sedentary',
    'activity_calories',
    'minutes_active'
]

# The requested two weeks of predictions
THE_FUTURE = pd.date_range('20181206', periods=14)

def get_predictions(df, target):
    df = df[['date', target]].rename({target: 'y', 'date': 'ds'}, axis=1)
    model = Prophet(yearly_seasonality=False, daily_seasonality=False, growth='linear')
    model.fit(df)
    return model.predict(pd.DataFrame(dict(ds=THE_FUTURE))).yhat


if __name__ == '__main__':
    _, df = prep_fitbit_data(get_fitbit_data())
    predictions = pd.DataFrame(
        {target: get_predictions(df, target) for target in TARGETS},
        index=THE_FUTURE
    )
    predictions.to_csv('predictions.csv', index=False)


