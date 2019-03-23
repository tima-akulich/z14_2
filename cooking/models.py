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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.title}'
