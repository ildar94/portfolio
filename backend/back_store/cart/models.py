from django.core.validators import MinValueValidator
from django.contrib.sessions.models import Session
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from shop.models import Product
from uuid import uuid4
# Create your models here.


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username', related_name='user', blank=True, null=True)
    created_at  =models.DateTimeField(auto_now_add=True)
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, blank=True, null=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1,validators=[MinValueValidator(1)])


    class Meta:
        unique_together = [['cart', 'product']]

