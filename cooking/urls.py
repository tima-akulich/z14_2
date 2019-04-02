from django.conf.urls import url
from django.urls import path
from cooking.views import index_view, register, recipe, create_recipe

urlpatterns = [
    path('', index_view, name='index'),
    path('register', register, name='register'),
    path('recipe_<id>', recipe, name='recipe'),
    path('new_recipe', create_recipe, name='new_recipe')
]
