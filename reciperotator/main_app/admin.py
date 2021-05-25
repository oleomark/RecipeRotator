from django.contrib import admin
from .models import Recipe, RecipeLog, Ingredient, Photo

# Register your modelss here.
admin.site.register(Recipe)
admin.site.register(RecipeLog)
admin.site.register(Ingredient)
admin.site.register(Photo)