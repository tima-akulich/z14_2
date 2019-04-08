from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from cooking.models import User, Recipe, RecipeReaction, ErrorLog


# Register your models here.

class ErrorLogAdmin(admin.ModelAdmin):
    list_display = ('exception_text', 'url',
                    'class_name', 'method',
                    'traceback', 'status_code')
    search_fields = ('url', 'class_name',
                     'method', 'status_code')

    list_filter = ('status_code','method', 'class_name', 'url')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'get_image',
                    'author', 'level', 'created_at',)
    search_fields = ('title', 'text')
    list_filter = ('level', 'created_at', 'author')
    fields = (
        ('title', 'text'),
        ('image', 'get_image'),
        'author', 'level'
    )
    save_on_top = True
    readonly_fields = ('get_image', 'author')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(
                f'<img style="height: 200px" src="{obj.image.url}"/>'
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
admin.site.register(ErrorLog, ErrorLogAdmin)

