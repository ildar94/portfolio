from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .serializers import *
#import django_filters.rest_framework
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
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
    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def dispatch(self, *args, **kwargs):
        return super(ProductListRetrieveViewSet, self).dispatch(*args, **kwargs)


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


class CartViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = UsersCart_test.objects.all()
        serializer = CartListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        print(request.data)
        serializer = CartListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})


# class CartViewSet(viewsets.ModelViewSet):
#     queryset = UsersCart_test.objects.all()
#     serializer_class = CartListSerializer
#     permission_classes = (IsAuthenticated,)
#     @action(detail=False, methods=['post'])
#     def add_to_cart(self, request, pk=None):
#         pass
        # q = User.objects.get(username=request.data['username'])
        # serializer = CartListSerializer(data=request.data)
        # if serializer.is_valid():
        #     user.set_password(serializer.validated_data['password'])
        #     user.save()
        #     return Response({'status': 'password set'})
        # else:
        #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


