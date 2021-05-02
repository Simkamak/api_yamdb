from django.db.models import Avg
from rest_framework import serializers

from .models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSafeSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False, read_only=True)
    genre = GenreSerializer(Genre, required=False, many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'name', 'year', 'rating', 'description', 'genre',
                  'category')
        model = Title

    def get_rating(self, obj):
        return obj.reviews.aggregate(Avg('score'))['score__avg']


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),
                                            slug_field='slug')
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(),
                                         many=True,
                                         slug_field='slug')
    rating = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'name', 'year', 'rating', 'description', 'genre',
                  'category')
        model = Title

    def get_rating(self, obj):
        return obj.reviews.aggregate(Avg('score'))['score__avg']
