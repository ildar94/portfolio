from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .serializers import *
import django_filters
from django_filters import rest_framework as filters

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.pagination import PageNumberPagination


class ProductFilter(filters.FilterSet):
    #min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    #max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    productstatus = django_filters.CharFilter(method = 'filter_badge')
    class Meta:
        model = Product
        fields = ['productstatus']
    def filter_badge(self, queryset, name, value):
        print("self ->>", self)
        print("queryset", queryset)
        print("name", name)
        print("value", value)
        resp = Product.objects.filter(productstatus__badge=value)
        print("resp ->>", resp)
        return resp


class ProductListRetrieveViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):

    queryset = Product.objects.all().order_by("id")
    def get_serializer_class(self):
        if self.action == 'list':
            serializer_class = ProductsSerializer
        else:
            serializer_class = ProductDetailSerializer

        return serializer_class

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
    # @method_decorator(vary_on_cookie)
    # @method_decorator(cache_page(60 * 60))
    # def dispatch(self, *args, **kwargs):
    #     return super(ProductListRetrieveViewSet, self).dispatch(*args, **kwargs)


class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Category.objects.all().order_by("id")
        serializer = CategoryListSerializer(queryset, many=True)
        respone  = Response(serializer.data)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, name=pk)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)


class MenuViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = MenuSerializer(queryset, many=True)
        print("serializer.data --->>>>>", serializer.data)
        return Response(serializer.data)
