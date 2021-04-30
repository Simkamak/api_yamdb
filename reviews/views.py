from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from titles.models import Title

from .models import Review
from .permissions import IsAbleToChange
from .serializers import CommentSerializer, ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAbleToChange, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs['title_id'])
        return title.reviews.all()

    def create(self, request, *args, **kwargs):
        serializer = ReviewSerializer(data=request.data)
        if not Review.objects.filter(
                title_id=get_object_or_404(
                    Title, id=kwargs['title_id']),
                author=request.user).exists():
            if serializer.is_valid():
                serializer.save(
                    title_id=get_object_or_404(
                        Title, id=kwargs['title_id']), author=request.user)
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response('Уже оставили отзыв',
                        status=status.HTTP_400_BAD_REQUEST)


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
