from rest_framework import filters, viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .permissions import IsYAMDBAdministrator
from .serializers import UserSerializer


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsYAMDBAdministrator]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', ]

    @action(detail=False, methods=['get', 'put', 'patch'], url_path='me',
            permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        user = self.request.user
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
