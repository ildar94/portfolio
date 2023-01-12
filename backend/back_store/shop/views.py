from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .serializers import *
import django_filters
from django_filters import rest_framework as filters
from django.db.models import Q
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
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    productstatus = django_filters.CharFilter(method='filter_badge')
    type = django_filters.CharFilter(method='filter_type')
    ## tip = django_filters.CharFilter(method = 'filter_attrs')
    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        query_keys = self.request.query_params.keys()
        print(query_keys)
        filter_keys = self.get_filters().keys()
        print(filter_keys)
        attr_keys = [key for key in query_keys if key not in filter_keys]
        print(attr_keys)
        list_of_filters = []
        for item in attr_keys:
            for value in self.request.query_params.getlist(item):
                field_name = FiltersByCategory.objects.get(alias=item).name
                lookup = f"attrs__{field_name}"
                list_of_filters.append({lookup: value})
        filterset = Q()
        for filter in list_of_filters:
            filterset.add(Q(**filter), Q.OR)

        queryset = queryset.filter(filterset).distinct()
        return queryset


    class Meta:
        model = Product
        fields = ['productstatus']

    def filter_attrs(self, queryset, name, value):
        print("name -->>>", name)
        field_name = FiltersByCategory.objects.get(alias=name).name
        lookup = f"attrs__{field_name}"
        return Product.objects.filter(**{lookup: value})

    def filter_badge(self, queryset, name, value):
        return Product.objects.filter(productstatus__badge=value)

    def filter_type(self, queryset, name, value):
        return Product.objects.filter(attrs__Тип=value)


class ProductListRetrieveViewSet(mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin,
                                 viewsets.GenericViewSet):
    queryset = Product.objects.all().order_by("id")

    # def get_queryset(self):
    #     # print(self.request.query_params)
    #     queryset = super().get_queryset()
    #     query_keys = self.request.query_params.keys()
    #     print(query_keys)
    #     filter_keys = self.filterset_class.get_filters().keys()
    #
    #     print(filter_keys)
    #     attr_keys = [key for key in query_keys if key not in filter_keys]
    #     print(attr_keys)
    #     list_of_filters = []
    #     for item in attr_keys:
    #         for value in self.request.query_params.getlist(item):
    #             field_name = FiltersByCategory.objects.get(alias=item).name
    #             lookup = f"attrs__{field_name}"
    #             list_of_filters.append({lookup: value})
    #     filterset = Q()
    #     for filter in list_of_filters:
    #         filterset.add(Q(**filter), Q.OR)
    #
    #     queryset = queryset.filter(filterset).distinct()
    #     return queryset

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
        respone = Response(serializer.data)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, slug=pk)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)


class MenuViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = MenuSerializer(queryset, many=True)
        print("serializer.data --->>>>>", serializer.data)
        return Response(serializer.data)
