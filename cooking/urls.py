from django.urls import path
from django.views.generic import CreateView

from cooking.views import FeedView, UserFeedView, CreateRecipeView, RecipeView, RegisterView, EditRecipe

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    path('recipe/<int:pk>/', RecipeView.as_view(),name="recipe"),
    path('create', CreateRecipeView.as_view(), name='create'),
    path('edit/<int:pk>', EditRecipe.as_view(), name='edit'),
    path('my-feed', UserFeedView.as_view(), name="user.feed"),
    path('auth/register', RegisterView.as_view(), name='signup')
]