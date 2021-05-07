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


def get_latest_news(ticker):
    try:
        url = 'https://api.tiingo.com/tiingo/news?tickers=appl'
        # url = 'https://api.tiingo.com/tiingo/news/{}=/'.format(ticker)
        response = requests.get(url, headers=headers)
        return response.json()[0]
    except:
        print("An exception with the news")

