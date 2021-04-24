from django.shortcuts import get_object_or_404
from rest_framework import (filters, generics, permissions, viewsets)

from .models import User
from .permissions import AdminPermission, IsOwner
from .serializers import UserSerializer


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', ]


class UserDetailAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        print(self.request.user)
        return get_object_or_404(User, email=self.request.user)
