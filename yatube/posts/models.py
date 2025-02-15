from django.db import models
from django.contrib.auth import get_user_model
from core.models import CreatedModel

User = get_user_model()

class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    def __str__(self):
        return f"{self.title}"
    

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='group'
    )

    def __str__(self):
        return str(self.id)

class Comment(CreatedModel):
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Текст вашего комментария'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self):
        return self.text[:15]


class Follow(CreatedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

