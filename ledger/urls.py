from django.urls import path, include
from . import views
from .views import RecipesInDatabase, RecipeContents

urlpatterns = [
    path('recipes/list', views.RecipesInDatabase, name = 'RecipeList'),
    path('recipe/<int:pk>', views.RecipeContents, name = 'RecipeDetail'),
]
app_name = 'ledger'