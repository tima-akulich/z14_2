from django.http import HttpResponse
from django.shortcuts import render

from cooking.models import Recipe, User

# Create your views here.


def hello_world(request, *args, **kwargs):
    name = request.GET.get('name', 'world')
    return HttpResponse(f'Hello, {name}')


def index_view(request, *args, **kwargs):
    name = request.GET.get('username') \
           or request.POST.get('username') \
           or 'world'

    recipes = Recipe.objects.all().order_by('-created_at')
    return render(
        request,
        template_name='index.html',
        context={
            'context_name': name,
            'recipes': recipes
        }
    )


def recipe_input(request, *args, **kwargs):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        level = request.POST.get('level')

        # Fix user_id add

        recipe = Recipe(
            title=title,
            text=text,
            author=User.objects.first(),
            level=level)
        recipe.save()

    recipes = Recipe.objects.all().order_by('-created_at')
    return render(
        request,
        template_name='recipe_input.html',
        context={
            'recipes': recipes,
        }
    )
