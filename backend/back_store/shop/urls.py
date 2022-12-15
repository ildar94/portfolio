from django.urls import path
from . import views
from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'products', views.ProductListRetrieveViewSet,basename='product')
router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'menu', views.MenuViewSet, basename='menu')


#urlpatterns = router
urlpatterns = [
    path('', include(router.urls))


]