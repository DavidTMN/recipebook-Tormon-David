from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe, Profile
from .forms import RecipeImageForm, RecipeForm

@login_required
def recipes_in_database(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, 'recipe_list.html', ctx)

@login_required
def recipe_contents(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {
        "recipe": recipe
    }
    return render(request, 'ingredient_list.html', ctx)

@login_required
def add_image(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeImageForm()
    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect("recipe_detail", pk=recipe.pk)
    ctx = {"form": form, "recipe": recipe}
    return render(request, 'add_image.html', {'form': form, 'recipe': recipe})
        
@login_required
def add_recipe(request, pk):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            author = Profile.objects.get(user=request.user)
            recipe.author = author
            recipe.save()
            return redirect('recipe_contents')
    return render(request, "add_recipe.html", {"form": form})
            
