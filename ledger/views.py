from .models import Ingredient, Recipe, RecipeIngredient
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def recipe_list(request):
    recipe = Recipe.objects.all()
    ctx = {
        'recipes': recipe
    }
    return render(request, 'recipe_list.html', ctx)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {
        'recipes': recipe
    }
    return render(request, 'recipes.html', ctx)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes.html'
