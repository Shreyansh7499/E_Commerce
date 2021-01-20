from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cart, Product, CartProduct
from rest_framework import viewsets
from .serializers import CartProductSerializer, ProductSerializer
from rest_framework.response import Response


@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user = request.user)
    cart_products = CartProduct.objects.filter(cart = cart)
    return render(request, 'shop/view_cart.html', { 'cart_products': cart_products })

@login_required
def view_product(request):
    products = Product.objects.all()
    return render(request, 'shop/view_product.html' , { 'products' : products})


class CartProductViewSet(viewsets.ViewSet):

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    
    def create(self, request):
        product = Product.objects.get(pk = request.data['pk'])
        cart, created = Cart.objects.get_or_create(user = request.user)
        cart_product, created = CartProduct.objects.get_or_create(product = product, cart = cart)
        cart_product.quantity += int(request.data['quantity'])
        cart_product.save()    
        serializer = CartProductSerializer(cart_product)
        return Response(serializer.data)