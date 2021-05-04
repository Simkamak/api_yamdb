from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from django.db.models import Avg

from .filters import SlugRangeFilter
from .models import Category, Genre, Title
from .permissions import AdminOrReadOnly
from .serializers import (CategorySerializer, GenreSerializer,
                          TitleSafeSerializer, TitleSerializer)


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    permission_classes = [AdminOrReadOnly]
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    permission_classes = [AdminOrReadOnly]
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')).order_by('id')
    permission_classes = [AdminOrReadOnly]
    serializer_class = TitleSafeSerializer
    filterset_class = SlugRangeFilter
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        method = self.request.method
        if method in ['POST', 'PATCH']:
            return TitleSerializer
        if method == 'GET':
            return TitleSafeSerializer
