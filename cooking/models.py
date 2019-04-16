from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


# class UserInfo(models.Model):
#     user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
#     avatar = models.ImageField(blank=True, null=True)
from django.urls import reverse


class User(AbstractUser):
    # ADMIN = 'admin'
    # MODERATOR = 'moderator'
    # SIMPLE_USER = 'user'

    # CHOICES = (
    #     (ADMIN, ADMIN),
    #     (MODERATOR, MODERATOR),
    #     (SIMPLE_USER, SIMPLE_USER)
    # )

    avatar = models.ImageField(blank=True, null=True)
    subscribers = models.ManyToManyField('self')
    # category = models.CharField(max_length=20, choices=CHOICES, default=SIMPLE_USER)


class Recipe(models.Model):
    external_id = models.CharField(max_length=32, null=True, blank=True)
    title = models.CharField(_('Название'), max_length=300)
    text = models.TextField(_('Текст'))
    image = models.ImageField(_('Картинка'), null=True, blank=True)
    external_image_url = models.URLField(null=True, blank=True)
    image_base64 = models.TextField(null=True, blank=True)
    author = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Автор'),
    )
    level = models.PositiveSmallIntegerField(_('Уровень'), blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.title}'

    def get_absolute_url(self):
        return reverse('recipe', args=(self.pk, ))

    @property
    def likes(self):
        return self.reactions.filter(status='like').count()

    @property
    def get_image(self):
        if self.external_image_url:
            return self.external_image_url
        return self.image_base64 or (self.image.url if self.image else '')

    class Meta:
        verbose_name = _('Рецепт')
        verbose_name_plural = _('Рецепты')
        ordering = ('-created_at',)
        # unique_together = (
        #     ('title', 'author'),
        # )
        # index_together = (
        #     ('title', 'author'),
        # )


class Comment(models.Model):
    text = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recipe = models.ForeignKey('cooking.Recipe', on_delete=models.CASCADE)


class BaseReaction(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'

    ALL = (LIKE, DISLIKE)

    STATUSES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike')
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=10, choices=STATUSES)

    class Meta:
        abstract = True


class RecipeReaction(BaseReaction):
    recipe = models.ForeignKey('cooking.Recipe', on_delete=models.CASCADE, related_name='reactions')


class CommentReaction(BaseReaction):
    comment = models.ForeignKey('cooking.Comment', on_delete=models.CASCADE)


class Repost(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=True, null=True)
