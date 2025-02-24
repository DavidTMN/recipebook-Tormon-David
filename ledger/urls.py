from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home, name = "home"),
    # path("basic/<int:num>", views.basicParams, name="basicParams"),
    path("recipes/list", views.recipeList, name = "recipeList")
]

app_name = "ledger"