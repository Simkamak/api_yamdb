from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Comment, Review, Title, User


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username', default=serializers.CurrentUserDefault())
    title_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Review

    def validate(self, data):
        author = self.context['request'].user
        title_id = get_object_or_404(
            Title, id=self.context[
                'request'].parser_context['kwargs'].get('title_id'))
        if ((self.context['request'].method == 'POST'
                and not Review.objects.filter(
                    title_id=title_id, author=author).exists())
                or self.context['request'].method == 'PATCH'):
            return data
        raise serializers.ValidationError('Уже оставили отзыв')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    review_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
