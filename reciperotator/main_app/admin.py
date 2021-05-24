from django.contrib import admin
from .models import Recipe, RecipeLog, Ingredient

# Register your modelss here.
admin.site.register(Recipe)
admin.site.register(RecipeLog)
admin.site.register(Ingredient)