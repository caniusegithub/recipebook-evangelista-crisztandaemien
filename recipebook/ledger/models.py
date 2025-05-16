from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length = 100)
    author = models.TextField(default="test profile")
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length = 100)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

class Profile(models.Model):
    name = models.CharField(max_length = 50)
    bio = models.TextField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# 1. ADDED RECIPEIMAGE MODEl
class RecipeImage(models.Model):
    image = models.ImageField(upload_to='recipe_images/', null=False, blank=False)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='images')