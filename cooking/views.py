from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseServerError, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, FormView

from cooking.forms import RecipeForm, RegistrationForm
from cooking.models import Recipe, User, RecipeReaction

from django.conf import settings


def error500(request, *args, **kwargs):
    raise Exception('Server error!!')


def error400(request, *args, **kwargs):
    return HttpResponse(status=400)


def like(request, *args, **kwargs):
    item_id = kwargs['item_id']
    reactions = RecipeReaction.objects.filter(user=request.user).filter(
        recipe_id=item_id
    ).all()
    if not reactions:
        reaction = RecipeReaction(
            recipe=Recipe.objects.filter(id=item_id).first(),
            user=request.user,
            status='like'
        )
        reaction.save()
    return redirect('feed')


class FeedView(ListView):
    paginate_by = settings.PAGE_SIZE
    template_name = 'recipe_list.html'
    queryset = Recipe.objects.all().order_by('-created_at')
    url_name = 'feed'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(
            object_list=object_list, **kwargs
        )
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


class CreateRecipeView(CreateView, LoginRequiredMixin):
    template_name = 'create_recipe.html'
    form_class = RecipeForm
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
        user = authenticate(
            request=self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        login(self.request, user)
        return super().form_valid(form)

