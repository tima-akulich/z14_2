from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView

from cooking.forms import RecipesForm, RegistrationForm
from cooking.models import Recipe, User
from django.conf import settings
# Create your views here.


class FeedView(ListView):
    paginate_by = settings.PAGE_SIZE
    template_name = 'recipe_list.html'
    queryset = Recipe.objects.all().order_by('-created_at')
    url_name = 'feed'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['feed_url'] = reverse(self.url_name)
        return context


class UserFeedView(FeedView, LoginRequiredMixin):
    url_name = 'user.feed'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


class RecipeView(DetailView):
    template_name = 'recipe.html'
    queryset = Recipe.objects.all()


class CreateRecipeView(CreateView):
    template_name = 'create_recipe.html'
    form_class = RecipesForm
    model = Recipe

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class RegisterView(FormView):
    template_name = 'registration/signup.html'
    form_class = RegistrationForm
    model = User
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        form.save()
        user = authenticate(self.request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, user)
        return super().form_valid(form)


class EditRecipe(UpdateView):
    template_name = 'create_recipe.html'
    form_class = RecipesForm
    model = Recipe

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
