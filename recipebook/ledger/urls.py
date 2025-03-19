from django.urls import path, include
from .views import recipe_list, recipe_detail

urlpatterns = [
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]
