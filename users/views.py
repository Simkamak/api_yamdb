from rest_framework import generics, permissions, viewsets, mixins, filters, views
from .serializers import UserSerializer
from .models import User
from .permissions import AdminPermission, IsOwner
from django.shortcuts import get_object_or_404


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', ]
    #http_method_names = ['get', 'post', 'head']



class UserDetailAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        print(self.request.user)
        return get_object_or_404(User, email=self.request.user)

    #def perform_create(self, serializer):
     #   user = get_object_or_404(User, id=self.kwargs['user_id'])
      #  serializer.save(username=self.request.user.username, post=post)












