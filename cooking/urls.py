from django.urls import path
from cooking.views import \
    hello_world,\
    index_view,\
    recipe_input

urlpatterns = [
    path('hello', hello_world, name='hello.world'),
    path('', index_view, name='index'),
    path('recipe_input', recipe_input, name='recipe_input')
]
