from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categories.models import Category
from .serializers import CategorySerializer
from .permissions import IsAdminReadOnly

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminReadOnly]
    serializer_class = CategorySerializer
    
    queryset = Category.objects.filter(published=True)
    lookup_fields = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
    