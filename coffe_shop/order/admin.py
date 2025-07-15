from django.contrib import admin
from .models import Order, OrderProduct

class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0

class OrdenAdmin(admin.ModelAdmin):
    model = Order 
    inlines = [
        OrderProductInlineAdmin
    ]

admin.site.register(Order, OrdenAdmin)
