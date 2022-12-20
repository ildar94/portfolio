from rest_framework_nested import routers
from django.contrib import admin
from django.urls import path, include
from .views import CartViewSet, CartItemViewSet

router = routers.DefaultRouter()
router.register(r'carts',CartViewSet, basename='cart')


cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-items-detail')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(cart_router.urls))
]