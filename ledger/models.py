from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:IngredientDetail', args=[self.pk])
    
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:RecipeDetail', args=[self.pk])
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients', null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe', null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)
    
class RecipeImage(models.Model):
    image = models.ImageField(upload_to='static/', null=False)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="image")
    