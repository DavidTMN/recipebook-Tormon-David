from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe, Ingredient, RecipeIngredient


def home(request):
    return HttpResponse("Hello World!")
# Create your views here.

def recipesInDatabase(request):
    recipes = Recipe.objects.all()
    return render(request, "recipelist.html", {"recipe": recipes})

def recipeContents(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, "ingredientList.html", {"recipe": recipe})