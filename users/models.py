from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class UserRole(models.TextChoices):
        USER = 'user'
        ADMIN = 'admin'
        MODERATOR = 'moderator'

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=UserRole.choices,
                            default=UserRole.USER)
    bio = models.TextField(blank=True)
    confirmation_code = models.TextField(null=True, default='')

    def __str__(self):
        return self.username
