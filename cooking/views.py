from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from cooking.models import Recipe

# Create your views here.


def hello_world(request, *args, **kwargs):
    name = request.GET.get('name', 'world')
    return HttpResponse(f'Hello, {name}')


def index_view(request, *args, **kwargs):

    recipes = Recipe.objects.all().order_by('-created_at')
    return render(
        request,
        template_name='index.html',
        context={
            'recipes': recipes
        }
    )


def create(request, *args, **kwargs):
    if 'button1' in request.POST:
        title = request.POST.get('title')
        text = request.POST.get('text')
        level = request.POST.get('levels')
        b = Recipe(title=title, text=text, level=level)
        b.save()
    return HttpResponseRedirect("/")
