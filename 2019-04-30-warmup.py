# IPython log file


pd.read_clipboard()
import pandas as pd
pd.read_clipboard()
pd.read_clipboard(sep=',')
df = pd.read_clipboard(sep=',')
df.head()
pd.__version__
pd.__version__
df.heaD()
df.head()
df[df.y == 'B'].x.max()
df[df.y == 'A'].x.mean()
df.groupby('y')
df.groupby('y').max()
df.groupby('y').mean()
df.groupby('y').min()
df.groupby('y').describe()
df.groupby('y').describe()
type(df.groupby('y').describe())
df.groupby('y').describe()
df.groupby('y').sum()
df.groupby('y').sum().C
df.groupby('y').sum()
df.groupby('y').sum()['C']
df.groupby('y').sum().loc[:, 'C']
df.groupby('y').sum().sort_values('y')
df.groupby('y').sum().sort_values('y').tail(1)
df.groupby('y').sum().loc['C']
df.groupby('y').agg('mean')
df.groupby('y').agg(['max', 'mean', 'min', 'sum'])
df.groupby('y').agg(['max', 'mean', 'min', 'sum'])
import numpy as np
df.groupby('y').agg(['max', np.mean, 'min', 'sum'])
df.groupby('y').agg(['max', np.mode, 'min', 'sum'])
df.head()
df.timestamp = pd.to_datetime(df.timestamp)
df.set_index('timestamp', inplace=True)
df.head()
df.groupby('y')
df.resample('6H')
df.resample('6H').mean()
df['2018-04-30']
df['2018-04-30'].y.min()
df['2018-04-30'].x.sum()
df.resample('D').y.min()
df.resample('D').y.max()
df.resample('D').sum()
df.resample('D').agg(['sum', 'mean', 'median'])
df.index.head()
df.index[:5]
df.index.date
df.index.day
df.index.month
df.groupby(df.date).sum()
df.groupby(df.index.date).sum()
df.groupby([df.index.date, 'y'])
df.groupby([df.index.date, 'y']).count()
df[df.y != 'C'].groupby([df.index.date, 'y']).count()
df.groupby([df.index.date, 'y']).count()
df.groupby(['y', df.index.date]).count()
df.groupby('y').min()
df.groupby('y').min().plot.bar()
import matplotlib.pyplot as plt
plt.show()
pd.Series([2, 3, -1], index=list('XYZ'))
pd.Series([2, 3, -1], index=list('XYZ')).plot.bar()
plt.show()
df.head()
df.x.plot()
plt.show()
for group in df.y.unique():
    data = df[df.y == group]
    plt.plot(data.index, data.x, label=group)
    
plt.legend()
plt.show()
