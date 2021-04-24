from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions

from .models import User


class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        role = request.user.role
        admin = User.objects.filter(role=User.UserRole.ADMIN)
        return role == admin


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.username == request.user.username
