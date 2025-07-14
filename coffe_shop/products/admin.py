from django.contrib import admin
from products.models import Product

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price', 'date']
    search_fields = ['name', 'price']

admin.site.register(Product, ProductAdmin)