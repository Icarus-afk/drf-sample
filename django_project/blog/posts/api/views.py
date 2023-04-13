from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from blog.utils import CustomAuthentication
from rest_framework.response import Response


class PostApiViewSet(ModelViewSet):
    authentication_classes = [CustomAuthentication]
    permission_class = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset1 = Post.objects.filter(published = True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'category__slug']
    
    def get(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data)
