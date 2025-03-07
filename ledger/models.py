from django.db import models
from django.urls import reverse
# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:ingredientDetail', args=[self.pk])
    
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipeDetail', args=[self.pk])
    
class RecipeIngredient(models.Model):
    Quantity = models.CharField(max_length=50)
    Recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients", null=True)
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe", null=True)