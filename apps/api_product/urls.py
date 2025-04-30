from django.urls import path
from . import views

urlpatterns = [
    # exemplo de rota
    path('produtos/', views.get_product, name='product-list'),
    path('produtos/1', views.post_product, name='product-list'),
]
