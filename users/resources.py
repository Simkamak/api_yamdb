from import_export import resources
from .models import CustomUser


class UserResource(resources.ModelResource):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role')
