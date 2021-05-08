from django.urls import path

from .views import portfolio, add_stock

urlpatterns = [
    path('', portfolio, name='portfolio'),
    path('templates/portfolio/add_stock.html', add_stock, name='add_stock')

]
