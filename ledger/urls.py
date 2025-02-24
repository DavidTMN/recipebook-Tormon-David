from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home, name = "home"),
    path("recipes/list", views.recipeList, name = "recipeList"),
    path("recipes/1", views.recipe1, name = "recipe1"),
    path("recipes/2", views.recipe2, name = "recipe2")
]

app_name = "ledger"