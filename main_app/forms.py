from django.forms import ModelForm
from .models import RecipeLog

class RecipeLogForm(ModelForm):
  class Meta:
    model = RecipeLog
    fields = ['date', 'review_name', 'recipe_use', 'review', 'rating']