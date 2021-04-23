from rest_framework import generics, permissions, viewsets, pagination, filters
from .serializers import UserSerializer
from .models import User
from .permissions import AdminPermission


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', ]
    #http_method_names = ['get', 'post', 'head']









