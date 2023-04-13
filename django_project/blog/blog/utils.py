from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
            validated_token = JWTAuthentication().get_validated_token(token)
            user = JWTAuthentication().get_user(validated_token)
            return (user, token)
        except:
            raise AuthenticationFailed('Invalid token')
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['id'] = user.id
        token['email'] = user.email
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        # Add custom claims to the response payload
        data['id'] = self.user.id
        data['email'] = self.user.email
        # Add any additional data you want to include in the response payload
        return data


