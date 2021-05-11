from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import json
from .models import StockDB
from .form import StockForm
# Create your views here.\

token = 'sk_9c552f5e68764a87aac37106892279c8'


def portfolio(request):
    if request.method == 'POST':
        ticker = request.POST['ticker']
        url = 'https://cloud.iexapis.com/stable/stock/{}/quote?token=sk_9c552f5e68764a87aac37106892279c8'.format(ticker)
        api_request = requests.get(url)
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'portfolio/home.html', {'api': api})
    else:
        return render(request, 'portfolio/index.html', {'ticker': 'testsymbol'})


def add_stock(request):
    # Handling POST request by user
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Stock added successfully")
            return redirect('add_stock')
    # No POST request found, then, display symbols from db
    else:
        ticker = StockDB.objects.all()
        output = []
        for ticker_item in ticker:
            url = 'https://cloud.iexapis.com/stable/stock/' + str(ticker_item) + '/quote?token=sk_9c552f5e68764a87aac37106892279c8'
            api_request = requests.get(url)
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."
        return render(request, 'portfolio/add_stock.html', {'ticker': ticker, 'output': output})


def delete_stock(request, stock_symbol):
    stock = StockDB.objects.get(ticker=stock_symbol)
    stock.delete()
    messages.success(request, f'{stock.ticker} has been deleted successfully.')
    return redirect('add_stock')

