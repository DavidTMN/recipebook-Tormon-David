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
        
RecipeIngredientFormSet = inlineformset_factory(
    Recipe,
    RecipeIngredient,
    fields=('ingredient', 'quantity'),
    extra=2,
    can_delete=False
)