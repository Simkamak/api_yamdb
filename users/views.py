from rest_framework import generics, permissions, viewsets, pagination
from .serializers import UserSerializer
from .models import User
from .permissions import CustomPermission


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = [pagination.PageNumberPagination]
    #permission_classes = [CustomPermission]





