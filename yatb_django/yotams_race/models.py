from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Source(models.Model):
    name = models.CharField(max_length=64, help_text='recipe source, book, site etc.', unique=True)
    link = models.URLField(
        max_length=128,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    name = models.CharField(max_length=64, default='', help_text='recipe name', unique=True, verbose_name='recipe')
    page_num = models.IntegerField(blank=True, null=True)
    recipe_source = models.ForeignKey(Source, on_delete=models.CASCADE)
    link = models.URLField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.name}'


class Making(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    score = models.FloatField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    effort = models.FloatField(validators=[MaxValueValidator(5), MinValueValidator(0)], null=True)


class Comment(models.Model):
    timestamp = models.DateTimeField()
    comment = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)