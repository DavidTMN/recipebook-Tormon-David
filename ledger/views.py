from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe, Profile
from .forms import RecipeImageForm, RecipeForm, RecipeIngredientFormSet

@login_required
def recipes_in_database(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, 'recipe_list.html', ctx)

@login_required
def recipe_contents(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {
        'recipe': recipe
    }
    return render(request, 'ingredient_list.html', ctx)

@login_required
def add_image(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeImageForm()
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect('ledger:recipe_detail', pk=recipe.pk)
    return render(request, 'add_image.html', {'form': form, 'recipe': recipe})
        
@login_required
def add_recipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        formset = RecipeIngredientFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            recipe = form.save(commit=False)
            formset.instance = recipe
            recipe.author = request.user
            recipe.save()
            formset.save()
            return redirect('ledger:recipe_detail', pk = recipe.pk)
    else:
        form = RecipeForm()
        formset = RecipeIngredientFormSet()
        
    return render(request, 'add_recipe.html', {'form': form, 'formset': formset})
            
