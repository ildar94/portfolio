from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from uuid import uuid4
# Create your models here.


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4())
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username', related_name='useruser')
    created_at  =models.DateTimeField(auto_now_add=True)
    # ordered = models.BooleanField(default=False)
    # total_price = models.FloatField(default=0)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # price = models.FloatField(default=0)
    # total_item = models.IntegerField(default=0)
    quantity = models.PositiveSmallIntegerField(default=1,validators=[MinValueValidator(1)])


    class Meta:
        unique_together = [['cart', 'product']]

# @receiver(post_save,sender=CartItem)
# def correct_price(sender, **kwargs):
#     cart_item = kwargs['instance']
#     products_price = Product.objects.get(id=cart_item.product.id)
#     cart_item.price= cart_item.quantity * float(products_price.price)
#     total_cart_items = CartItem.objects.filter(user=cart_item.user)
#     cart_item.total_item = len(total_cart_items)
#
#     cart = Cart.objects.get(id=cart_item.cart.id)
#     cart.total_price = cart_item.price
#     cart.save()

