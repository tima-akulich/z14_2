from django.contrib import admin
from cooking.models import Topic, Comment, Recipe, Repost, Friend,\
                            News, PeopleInGroup, RepostInGroup
# Register your models here.

admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Recipe)
admin.site.register(Repost)
admin.site.register(Friend)
admin.site.register(News)
admin.site.register(PeopleInGroup)
admin.site.register(RepostInGroup)