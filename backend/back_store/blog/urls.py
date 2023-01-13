from django.urls import path

from .views import Index_page, Backend_page, Frontend_page

urlpatterns = [
    path('', Index_page.as_view(), name='index' ),
    path('backend_developer', Backend_page.as_view() , name='backend_page'),
    path('frontend_developer', Frontend_page.as_view() , name='frontend_page')
]