from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path("recipes/list", views.recipesInDatabase, name = "recipeList"),
    path("recipe/<int:pk>", views.recipeContents, name = "recipeDetail"),
    
]
app_name = "ledger"