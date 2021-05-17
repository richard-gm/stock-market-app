from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from .forms import TickerSymbolForm
from .api import get_meta_data, get_latest_price, get_stocks_news, get_technical_analysis, get_news_sentiment_analysis


def index(request):
    if request.method == 'POST':
        form = TickerSymbolForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            return HttpResponseRedirect(ticker)
    else:
        form = TickerSymbolForm()
    return render(request, "stocks/index.html", {"form": form})


def ticker(request, tid):
    context = {}
    articles = [{
        "source": 'cnbc.com',
        "tags": 'stocks'
        }
    ]
    context['ticker'] = tid
    context['meta'] = get_meta_data(tid)
    context['price'] = get_latest_price(tid, request)
    context['news'] = get_stocks_news(tid, request)
    context['priceTarget'] = get_technical_analysis(tid)
    context['newsSentiment'] = get_news_sentiment_analysis(tid)
    return render(request, 'stocks/ticker.html', context)

