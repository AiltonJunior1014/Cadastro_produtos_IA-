# from django.urls import path
# from rest_framework.routers import DefaultRouter
# from .views import ProdutoViewSet

# router = DefaultRouter()

# router.register(r'produtos', ProdutoViewSet, basename='produto')

# urlpatterns = [
#     # exemplo de rota
#     path('produtos/', views.get_product, name='product-list'),
#     # path('produtos/', views.post_product, name='product-list'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, get_product, post_product, post_product_image
#, buscar_por_nome

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet, basename='produto')

urlpatterns = [
    path('', include(router.urls)),
    path('listar/', get_product, name='product-list'),
    path('buscar/', post_product, name='buscar-produto'),
    path('buscarImagem/', post_product_image, name='buscar-produto'),
]

