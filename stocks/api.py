# tingo api used
# API KEY = 5b49388fcb7f76ae2ed39277cd6d5200f70aa11b

import requests

headers = {
    'Content-type': 'application/json',
    'Authorization': 'Token 5b49388fcb7f76ae2ed39277cd6d5200f70aa11b'
}


def get_meta_data(ticker):
    url = 'https://api.tiingo.com/tiingo/daily/{}'.format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()


def get_latest_price(ticker):
    url = 'https://api.tiingo.com/tiingo/daily/{}/prices'.format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()[0]

