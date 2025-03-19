from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Recipe

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'ledger/recipe_list.html', {'recipes': recipes})

@login_required
def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'ledger/recipe_detail.html', {'recipe': recipe})