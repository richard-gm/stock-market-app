import requests
from urllib.error import HTTPError
from urllib.request import urlopen
from django.shortcuts import render
from django.contrib import messages
from bs4 import BeautifulSoup
import re

def web_scraping(request):
    url_trending = 'https://stocktwits.com/rankings'
    url_actives = 'https://stocktwits.com/rankings/most-active'
    rank = []
    trending = []
    name = []
    score = []
    price = []
    price_change = []

    # urlopen(URL_trending)
    # return render(request, "stocks/index.html", {"form": form})

    try:
        html = urlopen('https://stocktwits.com/rankings')
        bsObj =BeautifulSoup(html.read())
        print(bsObj.h1) #accessing tags
        print(bsObj.h2) #accessing tags
        print(bsObj.body.h3) #accessing tags
        bsObj2 = BeautifulSoup(html)
        tabledata = bsObj2.findAll("table",{"class":"st_3r-ycnL st_3QTv-Ni st_bRb7g_s st_29vRgrA"}) # fetches the entire table data DOM code
        print(tabledata)
        return render(request, "stocks/index.html", bsObj)
    except (HTTPError, AttributeError) as e:
        print(e)

