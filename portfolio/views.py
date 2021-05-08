from django.shortcuts import render
import requests
import json
# Create your views here.\

token = 'sk_9c552f5e68764a87aac37106892279c8'


def portfolio(request):
    if request.method == 'POST':
        ticker = request.POST['ticker']
        print(ticker)
        url = 'https://cloud.iexapis.com/stable/stock/{}/quote?token=sk_9c552f5e68764a87aac37106892279c8'.format(ticker)
        api_request = requests.get(url)
        print(api_request.content)
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'portfolio/home.html', {'api': api})
    else:
        return render(request, 'portfolio/index.html', {'ticker':'test symbol'})


def add_stock(request):
    return render(request, 'portfolio/add_stock.html', {})


