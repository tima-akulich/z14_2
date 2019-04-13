from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Case, IntegerField
from django.db.models import Count
from django.db.models import When
from django.shortcuts import redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, FormView

from cooking.forms import RecipeForm, RegistrationForm, ReactionForm
from cooking.models import Recipe, User

from django.conf import settings


class FeedView(ListView):
    paginate_by = settings.PAGE_SIZE
    template_name = 'recipe_list.html'
    queryset = Recipe.objects.all().order_by('-created_at')
    url_name = 'feed'

    def get_queryset(self):
        annotate_kwargs = {
            'likes_count': Count(
                Case(
                    When(
                        reactions__status='like',
                        then=1,
                    ),
                    output_field=IntegerField()
                )
            )
        }
        if self.request.user.is_authenticated:
            annotate_kwargs['liked'] = Count(
                Case(
                    When(
                        reactions__status='like',
                        reactions__user=self.request.user,
                        then=1,
                    ),
                    output_field=IntegerField()
                )
            )

        queryset = super().get_queryset().annotate(**annotate_kwargs)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(
            object_list=object_list, **kwargs
        )
        if self.request.GET.get('exception'):
            raise Exception("Smth bad")
        context['feed_url'] = reverse(self.url_name)
        return context


class UserFeedView(LoginRequiredMixin, FeedView):
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


class ReactionView(LoginRequiredMixin, CreateView):
    template_name = ''
    form_class = ReactionForm
    http_method_names = ['post']

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER') or reverse('feed')
