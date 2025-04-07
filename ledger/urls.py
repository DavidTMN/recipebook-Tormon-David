from django.urls import path, include
from . import views
from .views import RecipesInDatabase, RecipeContents, RecipeAdd

urlpatterns = [
    path('recipes/list/', views.RecipesInDatabase, name = 'RecipeList'),
    path('recipe/<int:pk>/', views.RecipeContents, name = 'RecipeDetail'),
    path('recipe/add/', views.RecipeAdd, name = 'RecipeAdd'),
]
app_name = 'ledger'