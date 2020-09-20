from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=64, default='', help_text='recipe name', unique=True)
    page_num = models.IntegerField()


class Making(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    score = models.FloatField(validators=[MaxValueValidator(5), MinValueValidator(0)])
