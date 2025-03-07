from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

# Register your models here.

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    
class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient