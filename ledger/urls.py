from django.urls import path, include
from . import views
from .views import recipes_in_database, recipe_contents, add_image, add_recipe

urlpatterns = [
    path('recipes/list/', views.recipes_in_database, name = 'RecipeList'),
    path('recipe/<int:pk>/', views.recipe_contents, name = 'RecipeDetail'),
    path('recipe/add/', views.add_image, name = 'AddImage'),
    path('recipe/add', add_recipe, name="AddRecipe")
]
app_name = 'ledger'