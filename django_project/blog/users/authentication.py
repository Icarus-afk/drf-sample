from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class DatabaseAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = JWTAuthentication().authenticate(request)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            user.jwt_refresh_token = str(refresh)
            user.jwt_access_token = str(refresh.access_token)
            user.save()
        return user or None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
