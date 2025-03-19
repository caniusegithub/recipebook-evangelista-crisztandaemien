from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length = 100)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)