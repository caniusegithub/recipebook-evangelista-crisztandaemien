from django.shortcuts import render

recipe_data = [
    {
        "name": "Recipe 1",
        "ingredients": [
            {"name": "tomato", "quantity": "3pcs"},
            {"name": "onion", "quantity": "1pc"},
            {"name": "pork", "quantity": "1kg"},
            {"name": "water", "quantity": "1L"},
            {"name": "sinigang mix", "quantity": "1 packet"}
        ],
        "link": "/recipe/1"
    },
    {
        "name": "Recipe 2",
        "ingredients": [
            {"name": "garlic", "quantity": "1 head"},
            {"name": "onion", "quantity": "1pc"},
            {"name": "vinegar", "quantity": "1/2cup"},
            {"name": "water", "quantity": "1 cup"},
            {"name": "salt", "quantity": "1 tablespoon"},
            {"name": "whole black peppers", "quantity": "1 tablespoon"},
            {"name": "pork", "quantity": "1 kilo"}
        ],
        "link": "/recipe/2"
    }
]

def recipe_list(request):
    return render(request, 'ledger/recipe_template.html', {"recipes": recipe_data, "page": "list"})

def recipe_detail(request, recipe_id):
    recipe_id = int(recipe_id) - 1
    if 0 <= recipe_id < len(recipe_data):
        recipe = recipe_data[recipe_id]
        return render(request, 'ledger/recipe_template.html', {"recipe": recipe, "page": "detail"})