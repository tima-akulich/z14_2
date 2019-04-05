from cooking.models import User
from django.utils.translation import ngettext_lazy


def my_context_processor(request):
    context = {
        'my_variable': 'Hello world',
        'users': User.objects.all()
    }
    if request.user.is_authenticated:
        context['auth'] = True
    count = int(request.GET.get('count', 0))
    context['some_string'] = ngettext_lazy('%(count)s копейка', '%(count)s копейка', count) % {'count': count}
    return context
