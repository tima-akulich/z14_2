from django.conf.urls import url
from django.urls import path
from cooking.views import hello_world, \
    index_view, example_json_response, \
    view_with_params, example_template, other_example_template

urlpatterns = [
    path('example1', example_template, name='example1'),
    path('example2', other_example_template, name='example2'),
    path('hello', hello_world, name='hello.world'),
    path('', index_view, name='index'),
    path('json-example', example_json_response, name='json'),
    path('someasdasasd-uri/<str:user_id>', view_with_params, name='with-params'),
    # url('^other-uri/\d+', view_with_params, name='other-name')
]
