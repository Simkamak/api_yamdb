from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'bio',
                  'role', 'confirmation_code')
        model = User


class UserAuthSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'username']


class UserConfirmationSerializer(UserAuthSerializer):
    confirmation_code = serializers.CharField(max_length=100,
                                              required=True)

    class Meta:
        model = User
        fields = ['confirmation_code', 'email', 'username']



