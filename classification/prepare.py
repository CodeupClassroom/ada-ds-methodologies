import acquire
# import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

df_iris = acquire.get_iris_data()

def drop_ids(df):
    df = df.drop(['species_id','measurement_id'], axis=1)
    return df

def rename_species(df):
    df = df.rename(columns={'species_name': 'species'})
    return df

def encode_species(df):
    le = LabelEncoder()
    le.fit(df['species'])
    df[['species']] = le.transform(df['species'])
    return df

def prep_iris(df):
    df = df.pipe(drop_ids).pipe(rename_species).pipe(encode_species)
    return df

df_titanic = acquire.get_titanic_data()

def handle_missing_vals(df):
    values = {'embark_town': 'Other', 'embarked': 'O'}
    df = df.fillna(value=values)
    return df

def drop_cols(df):
    df = df.drop(columns = 'deck')
    return df

def encode_embarked(df):
    le = LabelEncoder()
    le.fit(df.embarked)
    return df.assign(embarked = le.transform(df.embarked))

def split(df):
    train, test = train_test_split(df)
    return train, test

def scale_min_max(df):
    scaler = MinMaxScaler()
    scaler.fit(df[['fare','age']])
    df[['age','fare']] = scaler.transform(df[['fare','age']])
    return df

def prep_titanic(df):
    train, test = df.pipe(handle_missing_vals).pipe(drop_cols).pipe(encode_embarked).pipe(split)
    return train, test