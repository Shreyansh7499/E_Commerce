from django.contrib import admin
from .models import Cart, Product, CartProduct

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartProduct)