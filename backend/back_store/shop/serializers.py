from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProductsSerializer(serializers.ModelSerializer):
    lookup_field = ('pk',)
    category_id = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
class ProductAdditionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAdditionals
        #fields = '__all__'
        exclude = ['id', 'product']

class ProductPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['images']

class AboutProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutProduct
        fields = ['title', 'text_value']

class ProductMaxVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaxVersion
        fields = ['title', 'description']



class ProductDetailSerializer(serializers.ModelSerializer):
    additionals =ProductAdditionalSerializer(many=True)
    pictures = ProductPictureSerializer(many=True)
    about = AboutProductSerializer(many=True)
    max_version = ProductMaxVersionSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'

class ProductsPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["price"]


class returnnone():
    data = {"price": None}
class CategoryListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'

    def get_products(self, obj):
        product_price1 = Product.objects.filter(category_id=obj.id)
        #print(len(product_price1))
        if len(product_price1) != 0:
            product_price = Product.objects.filter(category_id=obj.id).order_by("price")[0]
            serializer = ProductsPriceSerializer(product_price)
        else:
            serializer = returnnone()
        return serializer.data


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True)
    class Meta:
        model = Category
        fields = '__all__'