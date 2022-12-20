from .models import MainPageBanner
from rest_framework import serializers


class MainPageBannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainPageBanner
        fields = '__all__'