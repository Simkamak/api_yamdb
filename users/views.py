from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail, BadHeaderError
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]





