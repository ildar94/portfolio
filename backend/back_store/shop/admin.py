from django.contrib import admin
from django.contrib.admin.options import ModelAdmin, TabularInline, StackedInline
from .models import *

# Register your models here.

# class ProductAdditionalsAdminInline(TabularInline):
#     extra = 1
#     model = ProductAdditionals






class ProductAdditionalsInline(StackedInline):
    extra = 1
    model = ProductAdditionals

class PictureInline(StackedInline):
    extra = 1
    model = Picture

class AboutProductInline(StackedInline):
    extra = 1
    model = AboutProduct

class ProductStatusInline(StackedInline):
    extra = 1
    model = ProductStatus

class ProductsStockInline(StackedInline):
    extra = 1
    model = ProductsStock






@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", )
    inlines = (ProductAdditionalsInline, PictureInline,AboutProductInline,ProductStatusInline,ProductsStockInline)#ProductAdditionalsInline







#
# @admin.register(product_attrs)
# class product_attrsAdmin(admin.ModelAdmin):
#     list_display = ("name",)
#
# @admin.register(product_attr_value)
# class product_attr_valueAdmin(admin.ModelAdmin):
#     list_display = ("value",)
#
