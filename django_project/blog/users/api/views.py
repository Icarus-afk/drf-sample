from rest_framework.views import APIView
from rest_framework import generics, permissions
from blog.utils import CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from users.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


class RegisterApi(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request):
        user = User.objects.get(id = request.user.id)
        serializer = UserUpdateSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        # get additional data to include in the response
        user_id = data['id']
        email = data['email']
        # add additional data to the response
        response_data = {
            'access_token': data['access'],
            'refresh_token': data['refresh'],
            'id': user_id,
            'email': email,
            # add any other additional data you want to include in the response
        }
        return Response(response_data, status=status.HTTP_200_OK)
