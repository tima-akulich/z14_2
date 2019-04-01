from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect
import json

from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST

from cooking.forms import MyFirstForm, RecipeForm
from cooking.models import Recipe

from django.core.paginator import Paginator

# Create your views here.


def hello_world(request, *args, **kwargs):
    name = request.GET.get('name', 'world')
    return HttpResponse(f'Hello, {name}')


@login_required
def recipe(request, *args, **kwargs):
    recipe_form = RecipeForm()
    if request.POST:
        title = request.POST.get('title')
        text = request.POST.get('text')
        level = request.POST.get('levels')
        b = Recipe(title=title, text=text, level=level)
        b.save()
        return HttpResponseRedirect("/")
    return render(
        request,
        template_name='create_recipe.html',
        context={
            'recipe_form': recipe_form
        }
    )



def index_view(request, *args, **kwargs):
    name = request.GET.get('username') \
           or request.POST.get('username') \
           or 'world'

    form = MyFirstForm()
    recipe_form = RecipeForm()
    if request.POST:
        form = MyFirstForm(request.POST)
        form.is_valid()

    recipes = Recipe.objects.all().order_by('-created_at')

    contact_list = Recipe.objects.all()
    paginator = Paginator(contact_list, 5)

    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    return render(
        request,
        template_name='index.html',
        context={
            'context_name': name,
            'recipes': recipes,
            'form': form,
            'recipe_form': recipe_form,
            'contacts': contacts
        }
    )


def example_template(request, *args, **kwargs):
    return render(request, template_name='example_page.html')


@login_required
@require_GET
def other_example_template(request, *args, **kwargs):
    return render(request, template_name='other_example_page.html')


def example_json_response(request, *args, **kwargs):
    return HttpResponse(json.dumps({
        "key": 123,
        "value": True,
        "list": [1,2,3],
        "dict": {
            "1": 2
        }
    }), content_type='application/json')


def view_recipe(request, user_id, **kwargs):
    recipes = Recipe.objects.get(pk=user_id)
    return render(
        request,
        template_name='recipe.html',
        context={"recipe_i": recipes}
    )


@login_required
def my_recipe(request, *args, **kwargs):
    contact_list = Recipe.objects.filter(author_id=request.user.id)
    paginator = Paginator(contact_list, 5)

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(
        request,
        template_name='index.html',
        context={"contacts": contacts}
    )



