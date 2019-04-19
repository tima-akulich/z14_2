from django.urls import path
from rest_framework.routers import DefaultRouter


from api.views import my_first_api_view, RecipeListView, RecipeRetrieveView, RecipeViewSet

router = DefaultRouter()
router.register('recipes-viewset', RecipeViewSet, basename='recipe')


urlpatterns = [
    path('', my_first_api_view, name='first-api'),
    path('recipes', RecipeListView.as_view(), name='recipes'),
    path('recipes/<int:pk>', RecipeRetrieveView.as_view(), name='recipes.retrieve'),
]

urlpatterns += router.urls
