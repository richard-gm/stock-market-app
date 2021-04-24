"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView

from src.views import (
    home_view,
    tweets_detail_view,
    tweets_list_view,
    profile,
    create_post_view,
    portfolio,
    dashboard
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('react/', TemplateView.as_view(template_name='react.html')),
    path('', home_view),
    path('dashboard', dashboard),
    path('profile/', profile),
    path('profile/create_post', create_post_view),
    path('tweets/', tweets_list_view),
    path('tweets/<int:tweet_id>', tweets_detail_view),
    path('portfolio', portfolio),
    path('profile/api/tweets/', include('src.urls')),  # API endpoints on this file
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
