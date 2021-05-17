# tingo api used
# API KEY = 5b49388fcb7f76ae2ed39277cd6d5200f70aa11b
# newsAPI = afcb0b2d3481429aa1c7456b38242f10
import json

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
import requests

headers = {
    'Content-type': 'application/json',
    'Authorization': 'Token 5b49388fcb7f76ae2ed39277cd6d5200f70aa11b'
}


def get_meta_data(ticker):
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&apikey=D6QELY8V0DPJIXIQ&symbol={}'.format(ticker)
    response = requests.get(url, headers=headers)
    # print(response.content) Uncomment this to see the data from the API
    return response.json()


def get_stocks_news(ticker, request):
    try:
        url = 'https://cloud.iexapis.com/stable/stock/{}/news/last/5?token=sk_9c552f5e68764a87aac37106892279c8'.format(ticker)
        response = requests.get(url)
        # print(response.content) Uncomment this to see the data from the API
        api_call = json.loads(response.content)[0]
        responseStatus = response.status_code
        if responseStatus == 404 or responseStatus == 302:
            messages.info(request, 'Ticker not found! - Insert a valid ticker')
            return HttpResponseRedirect("/")
            print(response.content)
        return api_call
    except:
        messages.info(request, 'Ticker not found in our API! - Please try another ticker')
        return HttpResponseRedirect("/")


def get_latest_price(ticker, request):
    url = 'https://api.tiingo.com/tiingo/daily/{}/prices'.format(ticker)
    response = requests.get(url, headers=headers)
    responseStatus = response.status_code
    if responseStatus == 404 or responseStatus == 302:
        messages.info(request, 'Ticker not found! - Insert a valid ticker')
        return HttpResponseRedirect("/")
        print(response.content)
    return response.json()[0]


def get_technical_analysis(ticker):
    url = 'https://finnhub.io/api/v1/scan/technical-indicator?symbol={}&resolution=60&token=c2fqdaiad3i850j6a340'.format(ticker)
    response = requests.get(url, headers=headers)
    responseStatus = response.status_code
    if responseStatus == 400:
        print(response.status_code)
        return HttpResponseRedirect("/")
    print(response.status_code)
    r = response.json()
    print(r['technicalAnalysis']['count'])
    return response.json()['technicalAnalysis']['count']


def get_news_sentiment_analysis(ticker):
    url = 'https://finnhub.io/api/v1/news-sentiment?symbol={}&resolution=60&token=c2fqdaiad3i850j6a340'.format(ticker)
    response = requests.get(url, headers=headers)
    responseStatus = response.status_code
    if responseStatus == 400:
        print(response.status_code)
        return HttpResponseRedirect("/")
    print(response.status_code)
    r = response.json()
    print(r['sentiment'])
    return response.json()['sentiment']