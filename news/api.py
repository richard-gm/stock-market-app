from django.shortcuts import render
import requests
import json

headers = {
    'Content-type': 'application/json',
    'Authorization': 'apiKey afcb0b2d3481429aa1c7456b38242f10',
    'category': 'business',
    'country': 'us'
}


def index(request):
    url = 'https://newsapi.org/v2/top-headlines?country=us&category=business'
    news_api_request = requests.get(url, headers=headers)
    api = json.loads(news_api_request.content)
    print(news_api_request.content)
    return render(request, 'news/index.html', {"api": api})


# General API for news
def news_by_ticker(ticker, request):
    url = 'https://newsapi.org/v2/everything?q={}&from=2021-05-07&sortBy=publishedAt'.format(ticker)
    news_api_request = requests.get(url, headers=headers)
    api = json.loads(news_api_request.content)
    # print(news_api_request.content)
    return render(request, 'news/index.html', {"api": api})

