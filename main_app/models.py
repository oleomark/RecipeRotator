from django.db import models
from django import forms
from django.urls import reverse
from django.contrib.auth.models import User


CUISINES = (('NA', 'North American'), ('SA','South American'), ('LA', 'Latin American'), ('AS', 'Asian'), ('EU', 'European'), ('MD', 'Mediterranean'), ('AF', 'African'))
# Create your models here.

RATINGS = (('One Star', '★'),('Two Star', '★★'),('Three Star', '★★★'),('Four Star', '★★★★'),('Five Star', '★★★★★'))
class Ingredient(models.Model):
    ingred_name = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    measurement = models.CharField(max_length=20, default="oz")

    def __str__(self):
        return self.ingred_name

    def get_absolute_url(self):
        return reverse('ingredients_detail', kwargs={'pk': self.id})    
class Recipe(models.Model): 
    name = models.CharField(max_length=100)
    cuisine = models.CharField(
        max_length=3,
        choices=CUISINES,
        default=CUISINES[0][0]
    )
    instructions = models.TextField(max_length=500)
    servingsize = models.IntegerField()
    calories = models.IntegerField()
    author = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): 
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={"recipe_id": self.id})

class RecipeLog(models.Model):
    recipe_use = models.BooleanField(default=True)
    date = models.DateField('Log Date')
    review_name = models.CharField(max_length=50)
    review = models.TextField(max_length=500)
    rating = models.CharField(
        max_length=20,
        choices = RATINGS,
        default = RATINGS[0][0]
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self): 
        return f"Photo for recipe_id: {self.recipe_id} @{self.url}"

    
