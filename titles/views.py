from django.shortcuts import get_list_or_404, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, status, viewsets
from rest_framework.response import Response

from .filters import SlugRangeFilter
from .models import Category, Genre, Title
from .permissions import AdminOrReadOnly
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    permission_classes = [AdminOrReadOnly]
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]

    def destroy(self, request, *args, **kwargs):
        print(request.data, args, kwargs)
        instance = get_object_or_404(Category, slug=kwargs['pk'])
        print(instance)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    permission_classes = [AdminOrReadOnly]
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]

    def destroy(self, request, *args, **kwargs):
        print(kwargs)
        instance = get_object_or_404(Genre, slug=kwargs['pk'])
        print(instance)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = [AdminOrReadOnly]
    serializer_class = TitleSerializer
    filterset_class = SlugRangeFilter
    filter_backends = [DjangoFilterBackend]

    def perform_create(self, serializer):
        category = get_object_or_404(Category,
                                     slug=self.request.data.get('category'))
        genre = get_list_or_404(Genre,
                                slug__in=self.request.data.getlist('genre'))
        serializer.save(category=category, genre=genre)

    def perform_update(self, serializer):
        category = None
        if 'category' in self.request.data:
            category = get_object_or_404(
                Category, slug=self.request.data.get('category')
            )
        genre = []
        if 'genre' in self.request.data:
            genre = get_list_or_404(
                Genre, slug__in=self.request.data.getlist('genre')
            )
        serializer.save(category=category, genre=genre)
