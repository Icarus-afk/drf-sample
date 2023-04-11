from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post
from .serializers import PostSerializer
from .permissions import IsAdminOrReadOnly

class PostApiViewSet(ModelViewSet):
    permission_class = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published = True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'category__slug']

    