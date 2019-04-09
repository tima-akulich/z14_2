from django.urls import path
from cooking.views import FeedView, UserFeedView, \
    RecipeView, CreateRecipeView, RegisterView, like, error500, error400

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    path('create', CreateRecipeView.as_view(), name='create'),
    path('recipe/<int:pk>/', RecipeView.as_view(), name='recipe'),
    path('my-feed', UserFeedView.as_view(), name='user.feed'),
    path('auth/register', RegisterView.as_view(), name='signup'),
    path('like_<int:item_id>', like, name='like'),
    path('error500', error500, name='error500'),
    path('error400', error400, name='error400'),
]
