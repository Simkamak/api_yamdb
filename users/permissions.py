from rest_framework import permissions
from .models import User
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.backends import BaseBackend


class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        role = request.user.role
        admin = User.objects.filter(role=User.UserRole.ADMIN)
        return role == admin




