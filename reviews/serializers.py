from rest_framework import serializers

from .models import Review, Comment, Title, Category, Genre


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    title_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    review_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name', read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genre
