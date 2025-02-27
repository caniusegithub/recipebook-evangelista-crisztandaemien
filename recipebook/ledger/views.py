from django.shortcuts import render

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_template.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get(Recipe, recipe_id)
    return render(request, 'recipe_template.html', {'recipe': recipe})