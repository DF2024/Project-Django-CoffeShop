from django.shortcuts import render



# Create your views here.

def product_list(request):
    contexto = {'nombre': 'Andrés'}

    return render(request, 'products_list/products_list.html', contexto)

