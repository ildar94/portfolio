from rest_framework import serializers
from .models import *

#---------Section for Product related models--------#

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


#---------END OF Section for Product related models--------#


class ProductsSerializer(serializers.ModelSerializer):
    lookup_field = ('pk',)
    #category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    images = ProductPictureSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'category', 'article', 'price', 'description', 'sales_price', 'sold_time', 'images', 'attrs']


class ProductDetailSerializer(serializers.ModelSerializer):
    additionals =ProductAdditionalSerializer(many=True)
    images = ProductPictureSerializer(many=True)
    about = AboutProductSerializer(many=True)
    max_version = ProductMaxVersionSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'



#--------------Category-----------#


class CategoryListSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'


    def get_price(self, obj) :
        if not Product.objects.filter(category=obj.slug).exists():
            price = None
        else:
            product_price = Product.objects.filter(category=obj.slug).order_by("price")[0]
            price = product_price.price
        return price



class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True)
    class Meta:
        model = Category
        fields = '__all__'

