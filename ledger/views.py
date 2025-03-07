from django.shortcuts import render
from .models import Recipe


def recipesInDatabase(request):
    recipes = Recipe.objects.all()
    return render(request, "recipelist.html", {"recipes": recipes})

def recipeContents(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, "ingredientList.html", {"recipe": recipe})