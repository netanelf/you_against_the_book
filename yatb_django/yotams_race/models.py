from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=64, default='', help_text='recipe name')
    page_num = models.IntegerField()


ONE_STAR = 1
TWO_STARS = 2
THREE_STARS = 3
FOUR_STARS = 4
FIVE_STARS = 5

RATING = (
    (ONE_STAR, _('One Star')),
    (TWO_STARS, _('Two Stars')),
    (THREE_STARS, _('Three Stars')),
    (FOUR_STARS, _('Four Stars')),
    (FIVE_STARS, _('Five Stars')),
)


class Making(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    score = models.PositiveSmallIntegerField(
        choices=RATING,
        default=FIVE_STARS
    )
