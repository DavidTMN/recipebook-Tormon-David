from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required

@login_required
def view_function(request):
    return render (request,)

def recipesInDatabase(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe_list.html", {"recipes": recipes})

def recipeContents(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, "ingredient_ist.html", {"recipe": recipe})