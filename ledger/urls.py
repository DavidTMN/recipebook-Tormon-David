from django.urls import path, include
from . import views
from .views import recipesInDatabase, recipeContents

urlpatterns = [
    path("recipes/list", views.recipesInDatabase, name = "recipeList"),
    path("recipe/<int:pk>", views.recipeContents, name = "recipeDetail"),
]
app_name = "ledger"