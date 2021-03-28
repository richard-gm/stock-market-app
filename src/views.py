import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
# django REST API framework
from rest_framework.response import Response  # Will handle the response rather than senting JSON Obj
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .forms import TweetForm
from .models import Tweet
from .serializer import TweetSerilizer
ALLOWED_HOSTS = settings.ALLOWED_HOSTS
# Create your views here.


def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "pages/home.html", context={}, status=200)


def login_page(request, *args, **kwargs):
    print(request.user)
    return render(request, "pages/login.html", context={}, status=200)


def portfolio(request, *args, **kwargs):
    print(request.user)
    return render(request, "pages/portfolio.html", context={}, status=200)


def profile(request, *args, **kwargs):
    return render(request, "pages/profile.html", context={}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post_view(request, *args, **kwargs):
    serializer = TweetSerilizer(data=request.POST)
    if serializer.is_valid(raise_exception=True):  # raise_exeption uses the build-in Response function to handle issues
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


@api_view(['GET'])
def tweets_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    serializer = TweetSerilizer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def tweets_detail_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.all()
    if not qs.exists():
        return Response({}, status=400)
    obj = qs.first()
    serializer = TweetSerilizer(obj)
    return Response(serializer.data, status=200)


def create_post_view_django(request, *args, **kwargs):
    # handling non-authenticated users
    user = request.user
    if not request.user.is_authenticated:
        user = None
        if request.is_ajax():
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        # do other form related logic
        obj.user = user  # user has been associated with the object created
        obj.save()  # saving the obj to db
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)  # 201 == created items
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
             return redirect(next_url)
        form = TweetForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'components/form.html', context={"form": form})


def tweets_list_view_django(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)


def tweets_detail_view_djando(request, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)
