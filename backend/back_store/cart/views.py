from django.shortcuts import render
from rest_framework import viewsets, permissions
from  .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
# Create your views here.



# class OrdersViewSet(viewsets.ModelViewSet):
#     queryset = Orders.objects.all().order_by('-id')
#     serializer_class = OrdersSerializer
#     permission_classes = (IsAuthenticated,)
#
#     def get_queryset(self):
#         user = self.request.user
#         queryset = self.queryset.filter(owner=user)
#         return queryset
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


class CartViewSet(ListModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin,
                  CreateModelMixin,
                  GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer



class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = (IsAuthenticated,)
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}

    def get_queryset(self):
        return CartItem.objects \
            .filter(cart_id=self.kwargs['cart_pk']) \
            .select_related('product')