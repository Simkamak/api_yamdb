from rest_framework import serializers
from django.db.models import Avg
from .models import Title, Category, Genre
from pytils.translit import slugify


class CategorySerializer(serializers.ModelSerializer):
    def validate(self, data):
        if 'slug' not in data:
            data['slug'] = slugify(data['name'])
        slug_exists = Category.objects.filter(slug=data['slug']).exists()
        if slug_exists:
            raise serializers.ValidationError(
                'Slug alredy exists')
        return data

    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if 'slug' not in data:
            data['slug'] = slugify(data['name'])
        slug_exists = Genre.objects.filter(slug=data['slug']).exists()
        if slug_exists:
            raise serializers.ValidationError(
                'Slug alredy exists')
        return data

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(
    #     slug_field='slug', read_only=True)
    # genre = serializers.SlugRelatedField(
    #     slug_field='slug', read_only=True)
    category = CategorySerializer(required=False, read_only=True)
    genre = GenreSerializer(Genre, required=False, many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'name', 'year', 'rating', 'description', 'genre',
                  'category')
        model = Title

    def get_rating(self, obj):
        return obj.reviews.aggregate(Avg('score'))['score__avg']