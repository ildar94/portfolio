from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, PassUpdateSerializer
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import  GenericViewSet


class CreateUser(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects
    serializer_class = UserSerializer
    pagination_class = None
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(CreateUser, self).get_permissions()


class ChangePassword(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = get_user_model().objects
    serializer_class = PassUpdateSerializer
    pagination_class = None