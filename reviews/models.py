from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Review(models.Model):
    title_id = models.ForeignKey(Title, related_name='reviews',
                                 on_delete=models.CASCADE)
    text = models.TextField('Отзыв')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='reviews')
    score = models.IntegerField(choices=(i, i) for i in range(0, 10))
    pub_date = models.DateTimeField('дата отзыва', auto_now_add=True)


class Comment(models.Model):
    review_id = models.ForeignKey(Review, related_name='comments',
                                  on_delete=models.CASCADE)
    text = models.TextField('Коментарий')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments')
    pub_date = models.DateTimeField('дата комментария', auto_now_add=True)
