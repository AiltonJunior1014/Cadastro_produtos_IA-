from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.post_product, name='get_all_produtc'),
]
