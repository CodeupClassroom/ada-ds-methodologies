import pandas as pd

def parse_sales_date(df):
    datetime_format = '%a, %d %b %Y %H:%M:%S %Z'
    df.sale_date = pd.to_datetime(df.sale_date, format=datetime_format, utc=True)
    return df

def set_date_index(df):
    return df.set_index('sale_date')

def add_date_parts(df):
    # year, quarter, month, day of month, day of week, weekend vs. weekday
    df['year'] = df.sale_date.dt.year
    df['quarter'] = df.sale_date.dt.quarter
    df['month'] = df.sale_date.dt.month
    df['day'] = df.sale_date.dt.day
    df['weekday'] = df.sale_date.dt.day_name().str[:3]
    df['is_weekend'] = df.weekday.str.startswith('S')
    return df

def improve_sales_data(df):
    df['sale_total'] = df.sale_amount * df.item_price
    return df.rename(columns={'sale_amount': 'quantity'})

def add_sales_difference(df):
    df['diff_from_last_day'] = df.sale_total.diff()
    return df

def aggregate_by_weekday(df):
    return df.groupby('weekday')[['sale_total', 'quantity']].agg(['median', 'sum'])

def prep_store_data(df):
    df = parse_sales_date(df)
    df = add_date_parts(df)
    df = improve_sales_data(df)
    df = add_sales_difference(df)
    return df

