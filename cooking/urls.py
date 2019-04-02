from django.urls import path
from cooking.views import FeedView, UserFeedView, \
    RecipeView, CreateRecipeView, RegisterView

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    path('create', CreateRecipeView.as_view(), name='create'),
    path('recipe/<int:pk>/', RecipeView.as_view(), name='recipe'),
    path('my-feed', UserFeedView.as_view(), name='user.feed'),
    path('auth/register', RegisterView.as_view(), name='signup'),
]
