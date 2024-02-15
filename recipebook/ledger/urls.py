from django.urls import path
from .views import recipes_list, recipes_1, recipes_2
urlpatterns = [
    path('recipes/list', recipes_list, name="recipes_list"),
    path('recipe/1', recipes_1, name="recipe_1"),
    path('recipe/2', recipes_2, name="recipe_2"),
    ]

app_name = "ledger"
