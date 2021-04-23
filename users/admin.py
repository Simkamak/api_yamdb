from django.contrib import admin
from .resources import UserResource
from import_export.admin import ImportMixin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(ImportMixin, UserAdmin):
    list_display = ('username', 'email', 'role', 'confirmation_code', )
    readonly_fields = [
        'date_joined',
    ]
    resource_class = UserResource


