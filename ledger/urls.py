from django.urls import path
from .views import RecipeListView, RecipeDetailView
urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name="recipes_list"),
    path('recipe/<int:pk>/detail', RecipeDetailView.as_view(), name="recipe"),
    ]

app_name = "ledger"