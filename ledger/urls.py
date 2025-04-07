from django.urls import path, include
from . import views
from .views import recipes_in_database, recipe_contents, recipe_add

urlpatterns = [
    path('recipes/list/', views.recipes_in_database, name = 'RecipeList'),
    path('recipe/<int:pk>/', views.recipe_contents, name = 'RecipeDetail'),
    path('recipe/add/', views.recipe_add, name = 'RecipeAdd'),
]
app_name = 'ledger'