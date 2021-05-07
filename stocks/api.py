# tingo api used
# API KEY = 5b49388fcb7f76ae2ed39277cd6d5200f70aa11b
# newsAPI = afcb0b2d3481429aa1c7456b38242f10
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
import requests

headers = {
    'Content-type': 'application/json',
    'Authorization': 'Token 5b49388fcb7f76ae2ed39277cd6d5200f70aa11b'
}


def get_meta_data(ticker):
    url = 'https://api.tiingo.com/tiingo/daily/{}'.format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()


def get_latest_price(ticker, request):
    url = 'https://api.tiingo.com/tiingo/daily/{}/prices'.format(ticker)
    response = requests.get(url, headers=headers)
    responseStatus = response.status_code
    if responseStatus == 404:
        messages.info(request, 'Ticker not found! - Insert a valid ticker')
        return HttpResponseRedirect("/")
    return response.json()[0]


# def get_latest_statements(ticker):
#     url = 'https://api.tiingo.com/tiingo/fundamentals/{}/statements?startDate=2021-1-30'.format(ticker)
#     response = requests.get(url, headers=headers)
#     responseStatus = response.status_code
#     if responseStatus == 400:
#         print(response.status_code)
#         return HttpResponseRedirect("/")
#     print(response.status_code)
#     return response.json()[0]


# def get_latest_news(ticker):
#     try:
#         # url = 'https://api.tiingo.com/tiingo/news?'
#         url = 'https://api.tiingo.com/tiingo/news/tickers={}'.format(ticker)
#         response = requests.get(url, headers=headers)
#         print(response.content)
#         return response.json()
#     except:
#         print("An exception with the news")

