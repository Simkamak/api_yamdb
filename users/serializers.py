from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        read_only_fields = ('author',)
        model = CustomUser