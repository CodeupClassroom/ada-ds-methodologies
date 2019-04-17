import os
import json
from datetime import datetime
from requests import get
import pandas as pd

RESPONSE_DIR = './responses'
BASE_URL = 'https://python.zach.lol'

def fetch_all_sales():
    next_page = '/api/v1/sales'
    while next_page is not None:
        response = get(BASE_URL + next_page).json()
        fp = open(RESPONSE_DIR + '/sales-{}.json'.format(response['payload']['page']), 'w')
        json.dump(response['payload']['sales'], fp)
        print('\r{} of {}'.format(response['payload']['page'], response['payload']['max_page']), end='')
        next_page = response['payload']['next_page']

def concatenate_sales_responses(save_csv=True):
    sales = []
    for json_file in os.listdir(RESPONSE_DIR):
        sales += json.load(open(RESPONSE_DIR + '/' + json_file))
    df = pd.DataFrame(sales)

    if save_csv:
        print(f'[{datetime.now()}] Writing csv')
        df.to_csv('sales.csv', index=False)
    return df

def get_sales_data():
    if os.path.exists('sales.csv'):
        print('Reading sales from local csv')
        return pd.read_csv('sales.csv')

    print('Fetching sales from api')
    if not os.path.exists(RESPONSE_DIR):
        os.mkdir(RESPONSE_DIR)
    fetch_all_sales()
    return concatenate_sales_responses(save_csv=True)

def get_items_data():
    if os.path.exists('items.csv'):
        print('Reading items from local csv')
        return pd.read_csv('items.csv')

    print('Fetching items from api')
    items = []
    next_page = '/api/v1/items'

    while next_page is not None:
        response = get(BASE_URL + next_page).json()
        print('item page #%s' % response['payload']['page'])
        items += response['payload']['items']
        next_page = response['payload']['next_page']
    df = pd.DataFrame(items)
    df.to_csv('items.csv', index=False)
    return df

def get_stores_data():
    if os.path.exists('stores.csv'):
        print('Reading stores from local csv')
        return pd.read_csv('stores.csv')

    print('Fetching store data from api')
    response = get(BASE_URL + '/api/v1/stores').json()
    df = pd.DataFrame(response['payload']['stores'])
    df.to_csv('stores.csv', index=False)
    return df

def get_all_data():
    sales = get_sales_data()
    stores = get_stores_data()
    items = get_items_data()

    sales.rename(columns={'store': 'store_id', 'item': 'item_id'}, inplace=True)
    df = pd.merge(sales, items, on='item_id')
    df = pd.merge(df, stores, on='store_id')

    return df

if __name__ == '__main__':
    df = get_all_data()
