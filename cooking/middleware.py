import traceback

from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed


def my_first_middleware(get_response):
    def _inner(request):
        print(request.META['HTTP_USER_AGENT'])
        response = get_response(request)
        print('Post request')
        return response
    return _inner


class MySecondMiddleware:
    def __init__(self, get_response):
        if not settings.DEBUG:
            raise MiddlewareNotUsed
        self.get_response = get_response

    def __call__(self, request):
        print('Class middleware')
        print(request.META['HTTP_USER_AGENT'])
        response = self.get_response(request)
        print('Post response', response.status_code)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('process view', view_func, view_args, view_kwargs)

    def process_exception(self, request, exception):
        print('process exception', exception, traceback.format_exc())

    def process_template_response(self, request, response):
        print('process template')
        return response
