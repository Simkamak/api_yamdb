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


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if (
                request.method in permissions.SAFE_METHODS
                and request.user.is_authenticated
        ):
            return True


class AnonymousReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True


class AuthUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return (
                    request.user.is_authenticated
                    and request.user.role == User.UserRole.USER
            )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class Moderator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return (
                    request.user.is_authenticated
                    and request.user.role == User.UserRole.MODERATOR
            )
