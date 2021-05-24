from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from .models import Recipe, Ingredient
from .forms import RecipeLogForm

# Create your views here.
class RecipeCreate(CreateView):
    model = Recipe
    fields = '__all__'
    # fields = ['name', 'cuisine', 'instructions', 'servingsize', 'calories', 'author', 'ingredients']
    # success_url = '/recipes/'
    def form_valid(self, form):
      form.instance.user = self.request.user  
      return super().form_valid(form)

class RecipeUpdate(UpdateView):
  model = Recipe
  fields = '__all__'

class RecipeDelete(DeleteView):
  model = Recipe
  success_url = '/recipes/'



def home(request): 
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def recipes_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', { 'recipes': recipes })

def recipes_detail(request, recipe_id): 
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients_recipe_doesnt_have = Ingredient.objects.exclude(id__in = recipe.ingredients.all().values_list('id'))
    recipelog_form = RecipeLogForm()
    return render(request, 'recipes/detail.html', {
         'recipe': recipe ,
         'recipelog_form': recipelog_form,
         'ingredients': ingredients_recipe_doesnt_have 
         })

def add_recipelog(request, recipe_id):
  form = RecipeLogForm(request.POST)
  if form.is_valid():
    new_recipelog = form.save(commit=False)
    new_recipelog.recipe_id = recipe_id
    new_recipelog.save()
  return redirect('detail', recipe_id=recipe_id)

def assoc_ingredient(request, recipe_id, ingredient_id):
  Recipe.objects.get(id=recipe_id).ingredients.add(ingredient_id)
  return redirect('detail', recipe_id=recipe_id)

def unassoc_ingredient(request, recipe_id, ingredient_id):
    Recipe.objects.get(id=recipe_id).ingredients.remove(ingredient_id)
    return redirect('detail', recipe_id=recipe_id)

class IngredientList(ListView):
    model = Ingredient


class IngredientDetail(DetailView):
    model = Ingredient


class IngredientCreate(CreateView):
    model = Ingredient
    fields = '__all__'


class IngredientUpdate(UpdateView):
    model = Ingredient
    fields = '__all__'


class IngredientDelete(DeleteView):
    model = Ingredient
    success_url = '/ingredients/'
