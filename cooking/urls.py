from django.conf.urls import url
from django.urls import path
from cooking.views import hello_world, \
    index_view, example_json_response, \
    example_template, other_example_template, recipe, view_recipe, my_recipe

urlpatterns = [
    path('example1', example_template, name='example1'),
    path('example2', other_example_template, name='example2'),
    path('recipe', recipe, name='recipe'),
    path('hello', hello_world, name='hello.world'),
    path('', index_view, name='index'),
    path('my_recipe', my_recipe, name='my_recipe'),
    path('json-example', example_json_response, name='json'),
    path('post/<str:user_id>', view_recipe, name='post'),
    # url('^other-uri/\d+', view_with_params, name='other-name')
]
