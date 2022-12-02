from rest_framework import status

from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response

# Create your views here.





class CartViewSet(ListModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin,
                  CreateModelMixin,
                  GenericViewSet):
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer
    lookup_field = 'user'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)





class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            print(" ---------POST-----------  ")
            print("request user --------->>>>>>>>>>>", self.request.user)
            print("request cockie --------->>>>>>>>>>>", self.request.COOKIES)
            print(" -------------------------  ")
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        print("-----------------GET----------------------")
        print("request user --------->>>>>>>>>>>", self.request.user)
        print("---------------------------------------------")
        return CartItemSerializer

    def get_serializer_context(self):
        cart_id = Cart.objects.get(user=self.kwargs['cart_user']).id
        return {'cart_id': cart_id}


    def get_queryset(self):
        cart_id = Cart.objects.get(user=self.kwargs['cart_user']).id
        return CartItem.objects \
            .filter(cart_id=cart_id) \
            .select_related('product')
