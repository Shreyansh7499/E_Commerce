from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)

class Product(models.Model):
    name = models.CharField(max_length = 40)    
    cost = models.IntegerField()

    def str(self):
        return str(self.name)


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0)
