from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin':
            return request.user.is_superuser
        elif request.user.role == 'moderator':
            return
        elif request.user.role == 'user':
            return

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user