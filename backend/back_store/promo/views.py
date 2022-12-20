from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from .models import MainPageBanner
from .serializers import MainPageBannerSerializer

# Create your views here.


class MainBanerViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = MainPageBannerSerializer
    queryset = MainPageBanner.objects.all().order_by("id")

