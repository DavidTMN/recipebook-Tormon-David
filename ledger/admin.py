from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

# Register your models here.

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ("name",)
    
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ("name",)
    inlines = [RecipeIngredientInline]
    
class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ("Quantity", "Recipe", "Ingredient")
    
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)