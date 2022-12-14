from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class User(AbstractUser):
    email =models.EmailField(unique=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    house_number = models.CharField(max_length=120, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    apartment  =models.PositiveIntegerField(blank=True, null=True)
    index = models.PositiveIntegerField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        db_table = 'auth_user'
    def __str__(self):
        return self.username