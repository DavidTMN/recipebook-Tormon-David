from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)