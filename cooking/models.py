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


class Comment(models.Model):
    author = models.ForeignKey(
        'auth.User', null=True, on_delete=models.SET_NULL
    )
    text = models.TextField()
    topic = models.ForeignKey(Topic,null=True, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(null=True, default=0)
    dislike = models.PositiveIntegerField(null=True, default=0)

    def __str__(self):
        return f'{self.author} - ' \
            f'{self.text[:15] +"..." if len(self.text) >=15 else self.text}'


class Recipe(models.Model):
    name_recipe = models.CharField(max_length=100)
    ingredients = models.TextField()
    text = models.TextField()
    topic = models.ForeignKey(Topic, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name_recipe}'


class Repost(models.Model):
    author = models.ForeignKey(
        'auth.User', null=True, on_delete=models.SET_NULL
    )
    topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150, default='')

    def __str__(self):
        return f'{self.topic}'


class News(models.Model):
    author = models.ForeignKey(
        'auth.User', null=True, on_delete=models.SET_NULL
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.title}'


class Friend(models.Model):
    author = models.ForeignKey(
        'auth.User', null=True, on_delete=models.SET_NULL
    )
    my_friend = models.ForeignKey(
        'auth.User', null=True, on_delete=models.SET_NULL, related_name='my_friend'
    )

    class Meta:
        unique_together = ('author', 'my_friend')

    def __str__(self):
        return f'{self.author}'


class PeopleInGroup(models.Model):
    group = models.ForeignKey(
        'auth.Group', on_delete=models.CASCADE
    )
    person = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.group.name} - {self.person.username}'

    class Meta:
        unique_together = ('group', 'person')


class RepostInGroup(models.Model):
    author = models.ForeignKey(
        'auth.User', null=True, on_delete=models.SET_NULL
    )
    group = models.ForeignKey(
        'auth.Group', on_delete=models.CASCADE
    )
    topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150, default='')

    def __str__(self):
        return f'{self.group.name}-{self.topic.title}'
