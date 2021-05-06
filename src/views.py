from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/feed.html")


def tweets_list_view(request, *args, **kwargs):
    return render(request, "tweets-files/list.html")


def tweets_detail_view(request, tweet_id, *args, **kwargs):
    return render(request, "tweets-files/details.html", context={"tweet_id": tweet_id})


def login_page(request, *args, **kwargs):
    print(request.user)
    return render(request, "pages/auth.html", context={}, status=200)


def portfolio(request, *args, **kwargs):
    print(request.user)
    return render(request, "pages/portfolio.html", context={}, status=200)


def dashboard(request, *args, **kwargs):
    print(request.user)
    return render(request, "pages/dashboard.html", context={}, status=200)


def profile(request, *args, **kwargs):
    return render(request, "pages/profile.html", context={}, status=200)

