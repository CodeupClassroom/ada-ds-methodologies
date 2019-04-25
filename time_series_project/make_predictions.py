# # Making Predictions
#
# This script will use the best model that came out of the modeling process (see
# the modeling notebook for more details on this) to make predictions for all
# the variables for the next two weeks of data.
#
# TODO:
#
# - we are predicting `minutes_active`, which is the combination of several
#   columns from the raw data. We should go back and predict each of these
#   components individually so that our predictions match the format in which we
#   were given the data.
# - we should also go back and make the column names from our output predictions
#   match up with the original data source so that the person who gave us the
#   data can more easily work with our predictions.

#
# ---
#

import os
from datetime import datetime

import pandas as pd
from fbprophet import Prophet

from acquire import get_fitbit_data
from prepare import prep_fitbit_data

def log(msg):
    print(f'[{datetime.now()} make_predictions.py] {msg}')

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

# Quiet the prophet training diagnostics. See
# https://github.com/facebook/prophet/issues/223
class suppress_stdout_stderr(object):
    '''
    A context manager for doing a "deep suppression" of stdout and stderr in
    Python, i.e. will suppress all print, even if the print originates in a
    compiled C/Fortran sub-function.
       This will not suppress raised exceptions, since exceptions are printed
    to stderr just before a script exits, and after the context manager has
    exited (at least, I think that is why it lets exceptions through).
    '''
    def __init__(self):
        # Open a pair of null files
        self.null_fds = [os.open(os.devnull, os.O_RDWR) for x in range(2)]
        # Save the actual stdout (1) and stderr (2) file descriptors.
        self.save_fds = [os.dup(1), os.dup(2)]

    def __enter__(self):
        # Assign the null pointers to stdout and stderr.
        os.dup2(self.null_fds[0], 1)
        os.dup2(self.null_fds[1], 2)

    def __exit__(self, *_):
        # Re-assign the real stdout/stderr back to (1) and (2)
        os.dup2(self.save_fds[0], 1)
        os.dup2(self.save_fds[1], 2)
        # Close the null files
        for fd in self.null_fds + self.save_fds:
            os.close(fd)


def get_predictions(df, target):
    log(f'- Predicting {target}')
    df = df[['date', target]].rename({target: 'y', 'date': 'ds'}, axis=1)
    model = Prophet(yearly_seasonality=False, daily_seasonality=False, growth='linear')
    with suppress_stdout_stderr():
        model.fit(df)
    return model.predict(pd.DataFrame(dict(ds=THE_FUTURE))).yhat


if __name__ == '__main__':
    log('Starting up')
    _, df = prep_fitbit_data(get_fitbit_data())
    log('Making predictions for {}'.format(', '.join(TARGETS)))
    predictions = [get_predictions(df, target) for target in TARGETS]
    predictions = pd.concat(predictions, axis=1, keys=TARGETS)
    predictions.index = THE_FUTURE
    log('Saving predictions to csv')
    predictions.to_csv('predictions.csv')
