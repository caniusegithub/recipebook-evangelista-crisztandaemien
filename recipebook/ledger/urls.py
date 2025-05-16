from django.urls import path, include
from .views import recipe_list, recipe_detail, add_recipe, add_recipe_image
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('recipe/add/', add_recipe, name='add_recipe'),
    path('recipe/<int:recipe_id>/add_image/', add_recipe_image, name='add_recipe_image'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
