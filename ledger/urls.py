from django.urls import path, include
from . import views
from .views import recipesInDatabase, recipeContents

urlpatterns = [
    path("recipes/list", views.recipesInDatabase, name = "recipeList"),
    path("recipe/<int:pk>", views.recipeContents, name = "recipeDetail"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/login", views.recipesInDatabase, name = "login")
    path("accounts/logout", views.recipesInDatabase, name = "logout")
    
    
]
app_name = "ledger"