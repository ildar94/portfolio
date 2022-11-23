from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import get_object_or_404
#from back_store.shop.serializers import UserSerializer, GroupSerializer
from .serializers import *
#import django_filters.rest_framework
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins


def MainShop(request):
    category = Category.objects.all()
    product = Product.objects.all()
    data = {
        'category' : category,
        'product' : product
    }
    return render(request, 'shop/index.html', data)



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







class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Category.objects.all().order_by("id")
        serializer = CategoryListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, name=pk)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)