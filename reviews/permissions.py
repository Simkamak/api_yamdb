from rest_framework import permissions

from .models import User


class IsAbleToChange(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.user.role == User.UserRole.ADMIN or
                request.user.role == User.UserRole.MODERATOR or
                obj.author == request.user)
