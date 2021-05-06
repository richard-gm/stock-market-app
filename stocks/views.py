from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from .forms import TickerSymbolForm
from .api import get_meta_data, get_latest_price

def index(request):
    if request.method == 'POST':
        form = TickerSymbolForm(request.POST)
        messages.info(request, 'Did1!')
        if form.is_valid():
            ticker = request.POST['ticker']
            return HttpResponseRedirect(ticker)
    else:
        messages.info(request, 'Did not work!')
        form = TickerSymbolForm()
    return render(request, "stocks/index.html", {"form": form})


def ticker(request, tid):
    context = {}
    context['ticker'] = tid
    context['meta'] = get_meta_data(tid)
    context['price'] = get_latest_price(tid)
    return render(request, 'stocks/ticker.html', context)


# def index(request):
#     return HttpResponse("Hi test")
#