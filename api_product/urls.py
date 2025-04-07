from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', Views/views.post_product, name='get_all_produtc'),
    path('api/token/', Views/TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', Views/TokenRefreshView.as_view(), name='token_refresh'),
]
