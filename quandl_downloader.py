import pandas as pd
import quandl
import os

quandl.ApiConfig.api_key = os.environ.get('QUANDL_API_KEY')


# Download list of contracts and corresponding Quandl codes
contracts = pd.read_csv('metadata.csv',
                        usecols=['Ticker', 'Quandl Code'],
                        index_col=['Ticker'])

count = len(contracts)
print('Number of files to download: {}'.format(count))

if 'data' not in os.listdir():
    os.mkdir('data')

counter = 0
for key, value in contracts.iterrows():
    counter += 1
    print('Downloading: {}, {} of {}'.format(key, counter, count))
    code = '{}1'.format(value.values[0])
    price = quandl.get(code)
    price.rename(columns={'Last': 'Close',
                        'Trade Date': 'Date'}, inplace=True)
    if 'Close' not in price.columns:
        price.rename(columns={'Settle': 'Close'}, inplace=True)
    price.to_csv('data/{}.csv'.format(key))
