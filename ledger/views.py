from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required

@login_required
def Recipes_In_Database(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

@login_required
def Recipe_Contents(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'ingredient_list.html', {'recipe': recipe})

@login_required
def Recipe_Add(request):
    return render(request, 'recipe_add.html', )