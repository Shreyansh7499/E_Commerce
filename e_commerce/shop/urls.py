from django.urls import path, include
from .views import CartProductViewSet, view_product, view_cart
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('CartProduct', CartProductViewSet, basename='CardProduct')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/<int:pk>/', include(router.urls)),
    path('products/', view_product, name='products'),
    path('cart/', view_cart, name='cart'),
]