from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Recipe, Ingredient, RecipeIngredient, Profile

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ("name",)
    inlines = [RecipeIngredientInline]
    search_fields = ("name",)
    list_filter = ("name",)
    
class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ("Recipe", "Ingredient", "Quantity",)
    list_filter = ("Recipe", "Ingredient", "Quantity",)
    
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    
class UserAdmin(admin.BaseUserAdmin):
    inlines = [ProfileInline,]
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)