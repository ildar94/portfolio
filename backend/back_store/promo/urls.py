from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from .views import MainBanerViewSet

router = routers.DefaultRouter()
router.register(r'mainbanner', MainBanerViewSet, basename='banner')






urlpatterns = [
    path('', include(router.urls)),
]