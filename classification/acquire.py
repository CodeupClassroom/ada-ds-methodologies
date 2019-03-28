# IPython log file


import pandas as pd
import numpy as np
import pydataset
pydataset.data('iris')
iris = pydataset.data('iris')
iris
iris.shape
iris.columns
[col.lower().replace('.', '_') for col in iris]
iris.columns = [col.lower().replace('.', '_') for col in iris]
iris.head()
iris.dtypes
iris.describe()
help(pd.read_excel)
pd.read_excel('/Users/zach/codeup/cohorts/ada/Excel_Stats.xlsx', sheet='Data')
df = pd.read_excel('/Users/zach/codeup/cohorts/ada/Excel_Stats.xlsx', sheet='Data')
df.head()
df.head()
df = pd.read_excel('/Users/zach/codeup/cohorts/ada/Excel_Stats.xlsx', sheet_name='Data')
df.head()
help(pd.read_excel)
df.head()
df_excel = df.head(100)
df_excel
df_excel_sample = df.head(100)
df_excel_sample
help(pd.read_excel)
df_excel_sample.columns[:5]
df.columns[:5]
df.types
df.dtypes
df.info()
type(df.info())
get_ipython().run_line_magic('pinfo', 'df.info')
list(df.loc[:, df.dtypes == 'object'])
object_columns = list(df.loc[:, df.dtypes == 'object'])
df.select_dtypes(include=['object'])
df.select_dtypes(include=['object']).columns
df.dtypes
df.dtypes[df.dtypes == 'object']
df.dtypes[df.dtypes == 'object']
df.dtypes[df.dtypes == 'object'].index
df.dtypes
df.select_dtypes(['int', 'float'])
df.select_dtypes(['int', 'float']).columns
df.select_dtypes('number').columns
for col in df[df.select_dtypes('number').columns]:
    r = df[col].max() - df[col].min()
    print(f'col: {r}')
    
for col in df[df.select_dtypes('number').columns]:
    r = df[col].max() - df[col].min()
    print(f'{col}: {r}')
    
    
df.apply(lambda s: s.max() - s.min())
df[df.select_dtypes('number').columns].apply(lambda s: s.max() - s.min())
pd.read_csv('https://classroom.google.com/u/0/w/Mjc3NjgxNDE5NjJa/t/all')
df = pd.read_csv('https://zach.lol/train.csv')
df.head()
df.shape
df.columns
df.dtypes
df.describe()
df.Occupancy.unique()
df.head()
df.head()
import env
url = f'mysql+pymysql://{env.username}:{env.password}@{env.hostname}/titanic_db'
df = pd.read_sql('SELECT * FROM passengers', url)
df.head()
df.shape
df.to_csv('titanic.csv')
get_ipython().system('ls')
pd.concat([df.head(), df.tail()])
pd.concat([df.head(), df.tail()])
df.dtypes
df.describe()
df.dtypes
df.sex.unique()
df.embarked.unique()
df.class.unique()
df['class']
df['class'].unique()
df.dtypes
df.groupby('deck').count()
df.deck.value_counts()
df.fare
df.fare.value_counts()
df.fare.value_counts(bins=3)
cols = ["survived", "pclass", "sibsp", "parch", "embarked", "class", "deck", "alone"]
for col in cols:
    print(f"{col}: {pd.Series(df_csv[col].value_counts().index.values).unique()[:5]}")
    
cols = ["survived", "pclass", "sibsp", "parch", "embarked", "class", "deck", "alone"]
for col in cols:
    print(f"{col}: {pd.Series(df[col].value_counts().index.values).unique()[:5]}")
    
cols = ["survived", "pclass", "sibsp", "parch", "embarked", "class", "deck", "alone"]
for col in cols:
    print(f"{col}: {pd.Series(df[col].value_counts().index.values).unique()[:5]}")
    
cols = ["survived", "pclass", "sibsp", "parch", "embarked", "class", "deck", "alone"]
for col in cols:
    print(f"{col:>10}: {pd.Series(df[col].value_counts().index.values).unique()[:5]}")
    
    
cols = ["survived", "pclass", "sibsp", "parch", "embarked", "class", "deck", "alone"]
for col in cols:
    print(f"{col:>10}: {pd.Series(df[col].value_counts().index.values).unique()[:5]}")
    
    
cols = ["survived", "pclass", "sibsp", "parch", "embarked", "class", "deck", "alone"]
for col in cols:
    print(f"{col:>10}: {', '.join(pd.Series(df[col].value_counts().index.values).unique()[:5])}")
    
    
    
cols = ["survived", "pclass", "sibsp", "parch", "embarked", "class", "deck", "alone"]
for col in cols:
    print(f"{col:>10}: {', '.join(pd.Series(df[col].value_counts().index.values).astype(int).unique()[:5])}")    
    
cols = ["survived", "pclass", "sibsp", "parch", "embarked", "class", "deck", "alone"]
for col in cols:
    print(f"{col:>10}: {', '.join(pd.Series(df[col].value_counts().index.values).astype(str).unique()[:5])}")    
    
df_csv2 = df_csv.drop(columns=(['passenger_id', 'age', 'fare']))

for col in df_csv2:
    if len(df_csv2[col].value_counts()) > 5:
        print(df_csv2[col].value_counts()[0:5])
    else:
        print(df_csv2[col].value_counts())
        
for col in df.drop(columns=(['passenger_id', 'age', 'fare'])):
    if len(df_csv2[col].value_counts()) > 5:
        print(df_csv2[col].value_counts()[0:5])
    else:
        print(df_csv2[col].value_counts())
        
for col in df.drop(columns=(['passenger_id', 'age', 'fare'])):
    if len(df[col].value_counts()) > 5:
        print(df[col].value_counts()[0:5])
    else:
        print(df[col].value_counts())
        
for col in df.drop(columns=(['passenger_id', 'age', 'fare'])):
    if len(df[col].value_counts()) > 5:
        print(df[col].value_counts()[:5])
    else:
        print(df[col].value_counts())
        
df.dtypes
for col in df.select_dtypes(object):
    print(col, (df[col].unique()[:5]))
    
for col in df.select_dtypes(object):
    print(col, (df[col].unique()[:5]))
    
{col: df[col].unique()[:5] for col in df.select_types(object)}
{col: df[col].unique()[:5] for col in df.select_dtypes(object)}
{col: list(df[col].unique())[:5] for col in df.select_dtypes(object)}
for col in df.select_dtypes(object):
    print(col, (df[col].unique()[:5]))
    
n = []
i = []
for t in titanic.columns[:]:
    n.append(titanic[t].unique())
    i.append(t)

unique = pd.DataFrame( n, index=i).T
unique.head()
n = []
i = []
for t in df.columns:
    n.append(df[t].unique())
    i.append(t)

pd.DataFrame( n, index=i).T
n = []
i = []
for t in df.columns:
    n.append(df[t].unique())
    i.append(t)

pd.DataFrame( n, index=i)
