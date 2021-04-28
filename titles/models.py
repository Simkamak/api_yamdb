from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.CharField('Название категории', max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField('Название произведения', max_length=100)
    year = models.IntegerField('Год выхода', blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    category = models.ForeignKey(Category,
                                 related_name='titles',
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True)
    # genre = models.ForeignKey(Genre,
    #                           on_delete=models.SET_NULL,
    #                           related_name='titles',
    #                           blank=True,
    #                           null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name
