from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from products.forms import product_form
from products.models import Product


# Create your views here.

class ProductFormView(generic.FormView):
    template_name = "add_product/add_product.html"
    form_class = product_form
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    


class product_list(generic.ListView):
    model = Product
    template_name = 'products_list/products_list.html'
    context_object_name = 'products'




