from django.contrib import admin

# Register your models here.

from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe 

admin.site.register(Recipe, RecipeAdmin)

