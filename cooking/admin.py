from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from cooking.models import User,\
    Recipe,\
    Comment,\
    RecipeReaction,\
    CommentReaction,\
    Repost

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(RecipeReaction)
admin.site.register(CommentReaction)
admin.site.register(Repost)
