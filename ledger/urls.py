from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path("", home, name = "home"),
    path("recipes/list", views.recipesInDatabase, name = "recipeList"),
    
]
app_name = "ledger"