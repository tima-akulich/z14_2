from django.db import models

# Create your models here.


class Topic(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(
        'auth.User', null=True, on_delete=models.SET_NULL
    )
    level = models.PositiveSmallIntegerField(blank=True, null=True)

    likes = models.PositiveSmallIntegerField(blank=True, null=True)
    dislikes = models.PositiveSmallIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.title}'


class Repost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    topic = models.ForeignKey(
        'Topic',
        null=True,
        on_delete=models.SET_NULL
    )
    author = models.ForeignKey(
        'auth.User',
        null=False,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.title} - {self.text} - {self.topic}'


class Comment(models.Model):
    text = models.TextField()
    topic = models.ForeignKey(
        'Topic',
        null=False,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        'auth.User',
        null=True,
        on_delete=models.SET_NULL
    )

    likes = models.PositiveSmallIntegerField(blank=True, null=True)
    dislikes = models.PositiveSmallIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.text} - {self.topic}'


class Subscription(models.Model):
    subuser = models.ForeignKey(
        'auth.User',
        null=False,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        'auth.User',
        null=False,
        on_delete=models.CASCADE,
        related_name='user'
    )

    def __str__(self):
        return f'{self.subuser} - {self.user}'

    class Meta:
        unique_together = ('subuser', 'user')
