from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)

# Register your models here.

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ("name",)
    
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ("name",)
    
class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ("recipe", "ingredient", "quantity")