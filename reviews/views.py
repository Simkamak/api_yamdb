from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticatedOrReadOnly)

from .models import Title, Review, Category, Genre
from .serializers import ReviewSerializer, CommentSerializer, CategorySerializer, TitleSerializer
from .permissions import IsOwnerOrReadOnly
from users.permissions import IsYAMDBAdministrator
from .pagination import CustomPagination


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)
    pagination_class = CustomPagination

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs['title_id'])
        return title.reviews.all()

    def perform_create(self, serializer):
        serializer.save(
            title_id=get_object_or_404(Title, id=self.kwargs['title_id']),
            author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)
    serializer_class = CommentSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs['title_id'])
        review = get_object_or_404(
            Review, title_id=title, id=self.kwargs['review_id'])
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs['review_id'])
        serializer.save(review_id=review, author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = (IsYAMDBAdministrator, IsAuthenticatedOrReadOnly)
    serializer_class = CategorySerializer
    pagination_class = CustomPagination



class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = (IsYAMDBAdministrator, IsAuthenticatedOrReadOnly)
    serializer_class = TitleSerializer
    pagination_class = CustomPagination


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    permission_classes = (IsYAMDBAdministrator, IsAuthenticatedOrReadOnly)
    serializer_class = TitleSerializer
    pagination_class = CustomPagination