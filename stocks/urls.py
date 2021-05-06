from django.urls import path

from .views import index, ticker

urlpatterns = [
    path('<str:tid>', ticker),
    path('', index)
]
