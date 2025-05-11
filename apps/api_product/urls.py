from django.urls import path
from rest_framework.routers import DefaultRouter
from . import ProdutoViewSet

router = DefaultRouter()

router.register(r'produtos', ProdutoViewSet, basename='produto')

urlpatterns = [
    # exemplo de rota
    # path('produtos/', views.get_product, name='product-list'),
    # path('produtos/', views.post_product, name='product-list'),
]
