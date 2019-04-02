from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from cooking.forms import RegistrationForm
from cooking.models import Recipe, User


def register(request, *args, **kwargs):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(
            request,
            template_name='registration/signup.html',
            context={
                'form': form
            }
        )
    else:
        return render(
            request,
            template_name='registration/signup.html',
            context={}
        )


def index_view(request, *args, **kwargs):
    username = request.GET.get('username', '')
    page_number = request.GET.get('page', 1)
    if not username:
        recipes = Recipe.objects.all().order_by('-created_at')
    else:
        recipes = Recipe.objects.filter(author__username=username)
    paginator = Paginator(recipes, 3)
    page = paginator.get_page(page_number)
    return render(
        request,
        template_name='index.html',
        context={
            'page': page,
            'username': username
        }
    )


def recipe(request, *args, **kwargs):
    recipe_id = request.path.split('_')[1]
    user_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(
        request,
        template_name='recipe.html',
        context={
            'recipe': user_recipe
        }
    )


@login_required
def create_recipe(request, *args, **kwargs):
    if request.POST:
        title = request.POST.get('title')
        text = request.POST.get('text')
        level = request.POST.get('level')
        user = User.objects.filter(username=request.user).first()

        new_recipe = Recipe(
            title=title,
            text=text,
            author=user,
            level=level)

        new_recipe.save()
        return redirect('index')

    return render(
        request,
        template_name='new_recipe.html',
        context={}
    )
