from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, permissions, viewsets

from .models import User
from .pagination import CustomPagination
from .permissions import IsYAMDBAdministrator
from .serializers import UserSerializer


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    pagination_class = CustomPagination
    permission_classes = [IsYAMDBAdministrator]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', ]


class UserDetailAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        print(self.request.user)
        return get_object_or_404(User, username=self.request.user)
