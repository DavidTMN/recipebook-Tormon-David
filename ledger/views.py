from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required

@login_required
def view_function(request):
    return render (request,)

def recipesInDatabase(request):
    recipes = Recipe.objects.all()
    return render(request, "recipeList.html", {"recipes": recipes})

def recipeContents(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, "ingredientList.html", {"recipe": recipe})