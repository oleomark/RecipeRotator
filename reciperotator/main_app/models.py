from django.db import models

# Create your models here.
class Recipe(models.Model): 
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    instructions = models.TextField(max_length=500)
    servingsize = models.IntegerField()
    author = models.CharField(max_length=100)

    def __str__(self): 
        return self.name