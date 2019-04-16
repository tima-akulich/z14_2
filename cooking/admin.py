from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from cooking.models import User, Recipe, RecipeReaction


# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'get_image',
                    'author', 'level', 'created_at',)
    search_fields = ('title', 'text')
    list_filter = ('level', 'created_at', 'author')
    fields = (
        ('title', 'text'),
        ('image', 'get_image', 'external_image_url'),
        'author', 'level'
    )
    save_on_top = True
    readonly_fields = ('get_image', 'author')

    def get_image(self, obj):
        if obj.get_image:
            return mark_safe(
                f'<img style="height: 200px" src="{obj.get_image}"/>'
            )
        return 'no image'
    get_image.short_description = 'Image'

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False

admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeReaction)

