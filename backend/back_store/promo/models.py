from django.db import models
from shop.models import Category
# Create your models here.

class MainPageBanner(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, to_field='slug')