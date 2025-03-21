from django.urls import path
from . import views
from .views import recipesInDatabase, recipeContents
import include

urlpatterns = [
    path("recipes/list", views.recipesInDatabase, name = "recipeList"),
    path("recipe/<int:pk>", views.recipeContents, name = "recipeDetail"),
    path("/accounts", include("django.contrib.auth.urls")),
]
app_name = "ledger"