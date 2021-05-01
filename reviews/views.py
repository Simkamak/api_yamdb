from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticatedOrReadOnly)

from .models import Review
from titles.models import Title
from .serializers import (
    ReviewSerializer, CommentSerializer)
from .permissions import IsAbleToChange


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAbleToChange, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs['title_id'])
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = get_object_or_404(Title, id=self.kwargs['title_id'])
        serializer.save(title_id=title_id, author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAbleToChange, IsAuthenticatedOrReadOnly)
    serializer_class = CommentSerializer

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs['title_id'])
        review = get_object_or_404(
            Review, title_id=title, id=self.kwargs['review_id'])
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs['review_id'])
        serializer.save(review_id=review, author=self.request.user)
