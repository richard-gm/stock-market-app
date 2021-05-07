from django.urls import path

from .views import index, ticker, index_by_ticker

# urlpatterns = [
#     path('<str:tid>', ticker),
#     path('', index)
# ]


urlpatterns = [
    path('<str:tid>', ticker),
    path('', index),
    path('test/', index_by_ticker),


]