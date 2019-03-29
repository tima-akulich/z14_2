from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect
import json

from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST

from cooking.forms import MyFirstForm, RecipeForm
from cooking.models import Recipe

# Create your views here.


def hello_world(request, *args, **kwargs):
    name = request.GET.get('name', 'world')
    return HttpResponse(f'Hello, {name}')


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
    return render(
        request,
        template_name='index.html',
        context={
            'context_name': name,
            'recipes': recipes,
            'form': form,
            'recipe_form': recipe_form
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


def view_with_params(request, user_id, **kwargs):
    # redirect()
    return HttpResponse(reverse('with-params', kwargs={'user_id': 1}))