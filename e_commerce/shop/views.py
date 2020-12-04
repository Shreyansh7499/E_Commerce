from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cart, Product, CartProduct
from rest_framework import viewsets
from .serializers import CartProductSerializer, ProductSerializer
from rest_framework.response import Response


@login_required
def view_cart(request):
    cart = Cart.objects.get_or_create(user = request.user)
    products = CartProduct.objects.filter(cart = cart)
    return render(request, 'shop/view_cart.html', { 'products': products })

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
        product = Product.objects.get(request.data['pk'])
        cart = Cart.objects.get_or_create(user = request.user)
        cart_product = CartProduct.objects.create(product = product, cart = cart, quantity = request.data['quantity'])
        serializer = CartProductSerializer(cart_product)
        return Response(serializer.data)