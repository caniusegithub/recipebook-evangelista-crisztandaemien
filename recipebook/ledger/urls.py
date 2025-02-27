from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/list/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]