from django.urls import path
from . import views
from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'registration', views.CreateUser,basename='register')
router.register(r'reset', views.ChangePassword,basename='reset')



#urlpatterns = router
urlpatterns = [
    path('', include(router.urls))


]

