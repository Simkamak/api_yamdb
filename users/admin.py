from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportMixin

from .models import User
from .resources import UserResource


@admin.register(User)
class CustomUserAdmin(ImportMixin, UserAdmin):
    list_display = ('username', 'email', 'role', 'confirmation_code',
                    'first_name', 'last_name')
    readonly_fields = [
        'date_joined',
    ]
    resource_class = UserResource
