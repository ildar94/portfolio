from django.contrib import admin
from .models import MainPageBanner
# Register your models here.

@admin.register(MainPageBanner)
class MainPageBannerAdmin(admin.ModelAdmin):
    list_display = ("title", "category")