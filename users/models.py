from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'admin'),
        ('user', 'user'),
        ('moderator', 'moderator'),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,
                            default='user')
    description = models.TextField(blank=True)
    confirmation_code = models.TextField(null=True, default='')

    def __str__(self):
        return self.email
