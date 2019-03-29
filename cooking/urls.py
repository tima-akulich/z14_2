from django.urls import path
from cooking.views import hello_world, index_view, recipe_create

urlpatterns = [
    path('hello', hello_world, name='hello.world'),
    path('', index_view, name='index'),
    path('create', recipe_create, name='create'),
]