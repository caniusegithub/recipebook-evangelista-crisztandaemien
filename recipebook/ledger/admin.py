from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

from .models import Ingredient, Recipe, RecipeIngredient, Profile, RecipeImage

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

# MODIFIED RECIPE ADMIN TO CONTAIN RECIPEIMAGES
class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeImageInline]

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class TheUserAdmin(UserAdmin):
    inlines = [ProfileInline]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

admin.site.unregister(User)
admin.site.register(User, TheUserAdmin)