from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Recipe
from .forms import RecipeForm, RecipeImageForm, RecipeIngredientForm

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'ledger/recipe_list.html', {'recipes': recipes})

@login_required
def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'ledger/recipe_detail.html', {'recipe': recipe})

# ADD RECIPE

@login_required
def add_recipe(request):
    recipeform = RecipeForm()
    ingredientform = RecipeIngredientForm()
    if request.method == 'POST':
        recipeform = RecipeForm(request.POST)
        ingredientform = RecipeIngredientForm(request.POST)
        if recipeform.is_valid() and ingredientform.is_valid():
            recipe = recipeform.save() 

            ingredient = ingredientform.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()

            return redirect('recipe_detail', recipe_id=recipe.id) 

    return render(request, 'ledger/recipe_add.html', {'recipeform': recipeform, 'ingredientform': ingredientform})

# ADD IMAGE

@login_required
def add_recipe_image(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeImageForm()

    return render(request, 'ledger/recipe_add_image.html', {'form': form, 'recipe': recipe})