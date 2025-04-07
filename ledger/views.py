from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required

def RecipesInDatabase(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

@login_required
def RecipeContents(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'ingredient_list.html', {'recipe': recipe})