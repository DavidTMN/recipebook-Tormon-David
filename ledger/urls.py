from django.urls import path, include
from . import views
from .views import recipes_in_database, recipe_contents, add_image, add_recipe

urlpatterns = [
    path('recipes/list/', views.recipes_in_database, name = 'recipe_list'),
    path('recipe/<int:pk>/', views.recipe_contents, name = 'recipe_detail'),
    path('recipe/<int:pk>/add_image/', views.add_image, name = 'add_image'),
    path('recipe/add/', add_recipe, name="add_recipe")
]
app_name = 'ledger'