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


class Error500Middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.log = False

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 500:
            self.log = True
        return response

    # def process_exception(self, request, exception):
    #
    #         print(request.status_code)
    #         print('####process exception', exception, traceback.format_exc())
