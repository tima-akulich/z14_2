from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from cooking.models import Recipe, User
import datetime
# Create your views here.


def hello_world(request, *args, **kwargs):
    name = request.GET.get('name', 'world')
    return HttpResponse(f'Hello, {name}')


def index_view(request, *args, **kwargs):
    name = request.GET.get('username') or request.POST.get('username') or 'world'
    recipes = Recipe.objects.all().order_by('-created_at')
    return render(
        request,
        template_name='index.html',
        context={
            'context_name' : name,
            'recipes' : recipes
        }
    )


def recipe_create(request, *args, **kwargs):
    if request.POST.get('title') and request.POST.get('text'):
        recipe = Recipe()
        recipe.title = request.POST.get('title')
        recipe.text = request.POST.get('text')
        recipe.level = request.POST.get('level')
        recipe.created_at = datetime.datetime.now()
        recipe.updated_at = datetime.datetime.now()
        recipe.save()
    return HttpResponseRedirect("/")
