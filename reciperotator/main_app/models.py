from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


CUISINES = (('NA', 'North American'), ('SA','South American'), ('LA', 'Latin American'), ('AS', 'Asian'), ('EU', 'European'), ('MD', 'Mediterranean'), ('AF', 'African'))
# Create your models here.

RATINGS = (("1", "1"),("2", "2"),("3", "3"),("4", "4"),("5", "5"))
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)

    def __str__(self):
        return self.name

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
    name = models.CharField(max_length=50)
    review = models.TextField(max_length=500)
    rating = models.CharField(
        max_length=5,
        choices = RATINGS,
        default = RATINGS[0][0]
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

    
