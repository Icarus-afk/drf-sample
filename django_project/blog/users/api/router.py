from django.urls import path
from .views import RegisterApi, UserView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/register', RegisterApi.as_view()),
    path('auth/login', CustomTokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('auth/me', UserView.as_view()),
]

