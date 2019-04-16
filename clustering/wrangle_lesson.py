# IPython log file


import pandas as pd
# Note that I've already setup my env.py file
import env
url = f'mysql+pymysql://{env.username}:{env.password}@{env.hostname}/mall_customers'
df = pd.read_sql('SELECT * FROM customers', url)
df.head()
df.set_index('customer_id')
df.set_index('customer_id').head()
df.set_index('customer_id', inplace=True)
df.head()
pd.concat([df.head(), df.tail()])
pd.concat([df.head(), df.tail()])
df.describe()
df.head()
df.gender.value_counts()
df.age.value_counts(bins=3)
df.age.value_counts(bins=[18, 26, 32, 40, 50, 80])
df.select_dtypes('number').head()
for col in df.select_dtypes('number'):
    print(col)
    print(df[col].value_counts(bins=4))
    
df.isna()
df.isna().sum()
df.describe()
df.describe(include=['age', 'annual_income'])
df.describe(include=['number'])
df.describe(include='all')
df.iloc[42, 'gender'] = np.nan
import numpy as np
df.iloc[42, 'gender'] = np.nan
df.loc[42, 'gender'] = np.nan
df[40:45]
df.describe(include='all')
df.gender.value_counts()
df.gender.value_counts(dropna=False)
df.dropna()
df.dropna().shape
df.shape
help(df.dropna)
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('matplotlib', 'qt')
import matplotlib.pyplot as plt
df.age.plot.hist()
df.annual_income.plot.hist()
df.spending_score.plot.hist()
df.gender.value_counts()
df.gender.value_counts().plot.bar()
df.annual_income.plot.box()
df.annual_income.quantile
get_ipython().run_line_magic('pinfo', 'df.annual_income.quantile')
q1 = df.annual_income.quantile(.25)
q3 = df.annual_income.quantile(.75)
iqr = q3 - q1
df.annual_income > (q3 + 1.5 * iqr)
df[df.annual_income > (q3 + 1.5 * iqr)]
df['is_annual_income_outlier'] = df.annual_income > (q3 + 1.5 * iqr)
df.head()
df.is_annual_income_outlier.sum()
df.annual_income - (q3 + 1.5 * iqr)
df.annual_income - (q3 + 1.5 * iqr)
df.annual_income.apply(lambda x: x - (q3 + 1.5 * iqr))
df.annual_income.apply(lambda x: max([x - (q3 + 1.5 * iqr), 0]))
df['annual_income_outliers'] = df.annual_income.apply(lambda x: max([x - (q3 + 1.5 * iqr), 0]))
df.annual_income_outliers.describe()
