from django.urls import path

from .views import portfolio, add_stock, delete_stock

urlpatterns = [
    path('add_stock/', add_stock, name='add_stock'),
    path('delete/<stock_symbol>', delete_stock, name='delete_stock'),
]
