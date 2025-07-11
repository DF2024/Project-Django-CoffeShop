from django.urls import path 
from products.views import product_list




urlpatterns = [
    path('lista-producto/', product_list, name='Lista productos')
]
