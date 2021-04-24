from rest_framework import permissions

from .models import User


class IsYAMDBAdministrator(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        print('has_permission:', request.user, request.user.role)
        return (
                request.user.role == User.UserRole.ADMIN or
                request.user.is_staff
        )
