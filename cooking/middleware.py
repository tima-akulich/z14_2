import traceback

from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
from django.utils.deprecation import MiddlewareMixin

from cooking.models import ErrorLog


class MySecondMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.response = self.get_response(request)
        return self.response

    def process_exception(self, request, exception):
        if self.response.status_code >= 500:
            ErrorLog.objects.create(
                exception_text=str(exception),
                class_name=exception.__class__.__name__,
                url=request.build_absolute_uri(),
                method=request.method,
                traceback=traceback.format_exc(),
                status_code=self.response.status_code
            )
