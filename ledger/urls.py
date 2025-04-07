from django.urls import path, include
from . import views
from .views import RecipesInDatabase, RecipeContents

urlpatterns = [
    path('recipes/list', views.RecipesInDatabase, name = 'recipeList'),
    path('recipe/<int:pk>', views.RecipeContents, name = 'recipeDetail'),
]
app_name = 'ledger'