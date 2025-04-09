from django import forms
from .models import RecipeImage, Recipe, RecipeIngredient
from django.forms import inlineformset_factory

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']
        
IngredientFormSet = inlineformset_factory(
    Recipe,
    RecipeIngredient,
    fields=('ingredient', 'quantity', 'unit'),
    extra=3,
    can_delete=False
)