from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField('Название категории', max_length=200)
    slug = models.SlugField(unique=True)


class Title(models.Model):
    name = models.CharField('Название произведения', max_length=200)
    year = models.IntegerField('Год выхода произведения')
    category = models.ForeignKey(Category, related_name='titles',
                                 on_delete=models.CASCADE)


class Review(models.Model):
    title_id = models.ForeignKey(Title, related_name='reviews',
                                 on_delete=models.CASCADE)
    text = models.TextField('Отзыв')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='reviews')
    score = models.IntegerField(choices=((i, i) for i in range(1, 11)))
    pub_date = models.DateTimeField('дата отзыва', auto_now_add=True)


class Comment(models.Model):
    review_id = models.ForeignKey(Review, related_name='comments',
                                  on_delete=models.CASCADE)
    text = models.TextField('Коментарий')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments')
    pub_date = models.DateTimeField('дата комментария', auto_now_add=True)
