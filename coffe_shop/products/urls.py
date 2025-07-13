from django.urls import path 
from products.views import product_list
from products.views import ProductFormView



urlpatterns = [
    path('lista/', product_list.as_view(), name='product_list'),
    path('agregar/', ProductFormView.as_view(), name="add_product")
]
