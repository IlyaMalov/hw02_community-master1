from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()
class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=30)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('posts:group', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title', ]



class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True
        )

    def __str__(self) -> str:
            return self.author

    class Meta:
        ordering = ['-pub_date', ]