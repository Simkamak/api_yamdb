from rest_framework import permissions

from .models import User


class AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        return (request.user.role == User.UserRole.ADMIN or
                request.user.is_staff)
