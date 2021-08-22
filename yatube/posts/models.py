from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(
        'Group',
        on_delete=models.PROTECT,
        blank=True, null=True,
        max_length=255,
        related_name='groups'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(max_length=400)

    def __str__(self):
        return str(self.title)
