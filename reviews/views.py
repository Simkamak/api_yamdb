from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticatedOrReadOnly)

from .models import Comment, Title, Review
from .serializers import ReviewSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
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
    queryset = Comment.objects.all()
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
