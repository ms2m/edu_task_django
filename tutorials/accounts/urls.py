from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import RegisterAPIView, LogOutApiView


urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='login_view'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('api/logout/', LogOutApiView.as_view(), name='logout_view'),
    path('api/register/', RegisterAPIView.as_view()),

]
