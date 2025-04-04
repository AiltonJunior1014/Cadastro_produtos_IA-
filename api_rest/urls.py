from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.post_product, name='get_all_produtc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
