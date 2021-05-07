from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json

from .forms import TickerSymbolNewsForm

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


def index_by_ticker(request):
    if request.method == 'POST':
        form = TickerSymbolNewsForm(request.POST)
        # messages.info(request, 'Did work!')
        if form.is_valid():
            ticker = request.POST['ticker']
            return HttpResponseRedirect(ticker)
    else:
        # messages.info(request, 'Did not work!')
        form = TickerSymbolNewsForm()
    return render(request, "news/news.html", {"form": form})


def ticker(request, tid):
    context = {}
    context['ticker'] = tid
    return render(request, 'news/ticker.html', context)


# def news_by_ticker(ticker, request):
#     ticker = 'tsla'
#     print(ticker)
#     url = 'https://newsapi.org/v2/everything?q={}&from=2021-04-07&sortBy=publishedAt'.format(ticker)
#     # url = 'https://newsapi.org/v2/top-headlines?country=us&category=business'
#     news_api_request = requests.get(url, headers=headers)
#     api = json.loads(news_api_request.content)
#     print(news_api_request.content)
#     return render(request, 'news/index.html', {"api": api})
#
#     url = 'https://newsapi.org/v2/everything?q={}&from=2021-04-07&sortBy=publishedAt'.format(ticker)
#     print(ticker)
#     # url = 'https://newsapi.org/v2/top-headlines?country=us&category=business'
#     news_api_request = requests.get(url, headers=headers)
#     api = json.loads(news_api_request.content)
#     print(news_api_request.content)
#     return render(request, 'news/index.html', {"api": api})