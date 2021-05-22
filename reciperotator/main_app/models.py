from django.db import models
from django.urls import reverse


CUISINES = (('NA', 'North American'), ('SA','South American'), ('LA', 'Latin American'), ('AS', 'Asian'), ('EU', 'European'), ('MD', 'Mediterranean'), ('AF', 'African'))
# Create your models here.
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

    def __str__(self): 
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={"recipe_id": self.id})
    
