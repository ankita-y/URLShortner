from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.Shortener.as_view(), name = 'Shortener'),
    # path('create/', views.ShortenerCreate.as_view(), name = 'ShortenerCreate'),
    path('', views.ShortenerCreate.as_view(), name = 'ShortenerCreate'),
    path('Shortener/', views.Shortener.as_view(), name = 'Shortener'),
    
]