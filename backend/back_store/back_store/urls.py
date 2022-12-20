"""back_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from shop import views as shop_views
from cart import views as cart_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
#from rest_framework_nested import routers


# router = routers.DefaultRouter()
# router.register(r'products', shop_views.ProductListRetrieveViewSet,basename='product')
# router.register(r'category', shop_views.CategoryViewSet, basename='category')
# router.register(r'carts',cart_views.CartViewSet)
#
# cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
# cart_router.register('items', cart_views.CartItemViewSet, basename='cart-items-detail')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/shop/', include('shop.urls')),
    path('api/v1/cart/', include('cart.urls')),
    path('api/v1/promo/', include('promo.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api//v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api//v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('__debug__/', include('debug_toolbar.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
