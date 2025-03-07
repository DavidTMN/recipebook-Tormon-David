from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe, Ingredient, RecipeIngredient


def home(request):
    return HttpResponse("Hello World!")
# Create your views here.

def recipesInDatabase(request):
    ingredients = RecipeIngredient.objects.all()
    recipes = RecipeIngredient.objects.filter(recipe_name="recipe1")
    
    return render(request, "ingredientList.html", {"ingredients": ingredients})