from rest_framework import serializers
from .models import Cart, Product, CartProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = ['name', 'cost']

class CartSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cart
        fields = ['user']

class CartProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    cart = CartSerializer()
    class Meta: 
        model = CartProduct
        fields = ['product', 'cart', 'quantity']
