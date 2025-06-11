from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

# Create your views here.


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html' # Path to your list template
    context_object_name = 'recipes' # variable name to use in the template


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html' # Path to your detail template
    context_object_name = 'recipe' # The variable name to use in the template