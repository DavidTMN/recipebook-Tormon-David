from django.urls import path, include
from . import views
from .views import Recipes_In_Database, Recipe_Contents, Recipe_Add

urlpatterns = [
    path('recipes/list/', views.Recipes_In_Database, name = 'RecipeList'),
    path('recipe/<int:pk>/', views.Recipe_Contents, name = 'RecipeDetail'),
    path('recipe/add/', views.Recipe_Add, name = 'RecipeAdd'),
]
app_name = 'ledger'