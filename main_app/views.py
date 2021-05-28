from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
import uuid
import boto3
from .models import Recipe, Ingredient, Photo
from .forms import RecipeLogForm

S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'recipe-rotator'

# Create your views here.

class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = '__all__'
    # fields = ['name', 'cuisine', 'instructions', 'servingsize', 'calories', 'author', 'ingredients']
    # success_url = '/recipes/'
    def form_valid(self, form):
      form.instance.user = self.request.user  
      return super().form_valid(form)

class RecipeUpdate(LoginRequiredMixin, UpdateView):
  model = Recipe
  fields = '__all__'

class RecipeDelete(LoginRequiredMixin, DeleteView):
  model = Recipe
  success_url = '/recipes/'



def home(request): 
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def recipes_index(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/index.html', { 'recipes': recipes })

@login_required
def recipes_detail(request, recipe_id): 
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients_recipe_doesnt_have = Ingredient.objects.exclude(id__in = recipe.ingredients.all().values_list('id'))
    recipelog_form = RecipeLogForm()
    return render(request, 'recipes/detail.html', {
         'recipe': recipe ,
         'recipelog_form': recipelog_form,
         'ingredients': ingredients_recipe_doesnt_have 
         })

@login_required
def add_recipelog(request, recipe_id):
  form = RecipeLogForm(request.POST)
  if form.is_valid():
    new_recipelog = form.save(commit=False)
    new_recipelog.recipe_id = recipe_id
    new_recipelog.save()
  return redirect('detail', recipe_id=recipe_id)

@login_required
def assoc_ingredient(request, recipe_id, ingredient_id):
  Recipe.objects.get(id=recipe_id).ingredients.add(ingredient_id)
  return redirect('detail', recipe_id=recipe_id)

@login_required 
def unassoc_ingredient(request, recipe_id, ingredient_id):
    Recipe.objects.get(id=recipe_id).ingredients.remove(ingredient_id)
    return redirect('detail', recipe_id=recipe_id)

@login_required
def add_photo(request, recipe_id): 
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      Photo.objects.create(url=url, recipe_id=recipe_id)
    except: 
      print('An error occurred uploading file to S3')
  return redirect('detail', recipe_id=recipe_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient


class IngredientDetail(LoginRequiredMixin, DetailView):
    model = Ingredient


class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = '__all__'


class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    fields = '__all__'


class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    success_url = '/ingredients/'
