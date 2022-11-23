from django.db import models
#from django.utils.text import slugify
from pytils.translit import slugify
from django.contrib.postgres.fields import JSONField
from django.contrib.auth import get_user_model
import os
from django.conf import settings
# Create your models here.

#################################JSONField-technology###################################



class Category(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    icon = models.CharField(max_length=100, null=True,blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
def product_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

    this_path = os.getcwd
    path = os.path.join(settings.MEDIA_ROOT,  r'images')
    path += r"\\products\\" + str(instance.slug) + r"\\" + filename
    return path
def product_picture_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    this_path = os.getcwd
    path = os.path.join(settings.MEDIA_ROOT,  r'images')
    path += r"\\products\\" + str(instance.product.slug) + r"\\" + filename
    return path


class Product(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    article = models.IntegerField(blank=False)
    price = models.FloatField()
    product_image = models.ImageField(null=True, blank=True, upload_to=product_directory_path)
    description = models.TextField(null=True, blank=True)
    sales_price = models.FloatField(null=True,blank=True)
    sold_time = models.IntegerField(null=True, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    attrs = models.JSONField(null=True, blank=True)
    #product_addtitionals = models.ManyToManyField(ProductAdditionals)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductAdditionals(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='additionals', blank=True, null=True)
    complectation = models.JSONField(null=True, blank=True)
    colors = models.JSONField(null=True, blank=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    prod_option = models.CharField(max_length=255, blank=True, null=True)
    prod_variants  = models.TextField(blank=True, null=True)
    prod_option2 = models.CharField(max_length=255, blank=True, null=True)
    prod_variants2 = models.TextField(blank=True, null=True)
    prod_option3 = models.CharField(max_length=255, blank=True, null=True)
    prod_variants3 = models.TextField(blank=True, null=True)
    editions = models.JSONField(null=True, blank=True)




class Picture(models.Model):
    images = models.ImageField(null=True,blank=True, upload_to=product_picture_directory_path)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,  related_name='pictures')


class AboutProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='about' )
    title = models.CharField(max_length=255, null=True, blank=True)
    text_value = models.TextField(null=True, blank=True)



class ProductStatus(models.Model):
    STATUSBADGE = [
        ('hit', 'HIT'),
        ('latest', 'latest')
    ]
    HIT = 'HIT'
    LATEST = 'latest'
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.CharField(max_length=100,blank=True,null=True)
    badge = models.CharField(max_length=10, choices=STATUSBADGE, default=HIT, blank=True, null=True)



class ProductsStock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=255, blank=True, null=True)
    quan_stock = models.PositiveIntegerField(null=True, blank=True)



class ProductMaxVersion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="max_version")
    title = models.CharField(max_length=255, null=True)
    icon = models.ImageField(null=True,blank=True, upload_to=product_picture_directory_path)
    description = models.TextField(null=True)




class Cart(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
    )
    product = models.ManyToManyField(Product)

##################################EAV-technology########################################

#
#
# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, unique=True, blank=True)
#     icon = models.ImageField(null=True,blank=True, upload_to='images/')
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super(Category, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.name
#
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, unique=True, blank=True)
#     article = models.IntegerField(blank=False)
#     price = models.FloatField()
#     description = models.TextField(null=True, blank=True)
#     sales_price = models.FloatField(null=True,blank=True)
#     sold_time = models.IntegerField(null=True, blank=True)
#     category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
#
#
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super(Product, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.name
#
#
#
#
#
# class product_attrs(models.Model):
#     category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
#
# class product_attr_value(models.Model):
#     attrs_id = models.ForeignKey(product_attrs, on_delete=models.PROTECT)
#     product = models.ForeignKey(Product, on_delete=models.PROTECT())
#     value = models.CharField(max_length=255)
#     opt_value = models.CharField(max_length=255, blank=True, null=True)
#
#     def __str__(self):
#         return self.value
