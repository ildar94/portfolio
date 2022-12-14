from rest_framework import status
from rest_framework.views import APIView
from .models import Cart, CartItem
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from psycopg2.errors import UniqueViolation
from django.db.utils import IntegrityError

# Create your views here.




class CartViewSet(ListModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin,
                  CreateModelMixin,
                  GenericViewSet):
    pagination_class = None

    def concast_cart(self):
        if Cart.objects.filter(session=self.request.session.session_key):
            cart_id_anonym = Cart.objects.get(session=self.request.session.session_key).id
            cart_id_user = Cart.objects.get(user=self.request.user).id
            if CartItem.objects.filter(cart_id=cart_id_anonym):
                for item in CartItem.objects.filter(cart_id=cart_id_anonym):
                    try:
                        item.cart_id=cart_id_user
                        item.save()
                    except UniqueViolation:
                        print("already exist")
                    except IntegrityError:
                        print("integerity -> already_exist product ->>>", item.product_id )
                        item.delete()

    def create(self, request, *args, **kwargs):
        if  request.user.is_authenticated !=True:
            if  request.session.session_key is None:
                request.session.save()
            session = {'session_key': request.session.session_key}
            serializer = CartAnonymousSerializer(context=session)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def check_exist(self):
        if self.request.session.session_key:
            try:
                Cart.objects.get(session=self.request.session.session_key)
            except Cart.DoesNotExist:
                self.create(self.request)
        else:
            self.request.session.save()
            self.create(self.request)
    def get_queryset(self):
        if self.request.user.is_authenticated != True:
            self.check_exist()
            return Cart.objects.filter(session=self.request.session.session_key)
        self.concast_cart()
        return Cart.objects.filter(user=self.request.user)
    def get_serializer_class(self):
        if self.request.user.is_authenticated !=True:
            self.check_exist()
            return CartAnonymousSerializer
        self.concast_cart()
        return CartSerializer



class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        cart_id = Cart.objects.get(id=self.kwargs['cart_pk']).id
        return {'cart_id': cart_id}


    def get_queryset(self):
        cart_id = Cart.objects.get(id=self.kwargs['cart_pk']).id
        return CartItem.objects \
            .filter(cart_id=cart_id) \
            .select_related('product')
