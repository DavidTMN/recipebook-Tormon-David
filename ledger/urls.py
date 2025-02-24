from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home, name = "home"),
    path("basic/<int:num>", views.basicParams, name="basicParams"),
    path("/recipes/list", views.recipeList, name = "recipeList"),
    path("/recipes/1", views.ingredientList, name = "recipe1"),
    path("/recipes/2", views.ingredientList, name = "recipe2")
]

app_name = "ledger"