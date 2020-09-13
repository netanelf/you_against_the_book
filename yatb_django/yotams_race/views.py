from django.shortcuts import render
from yotams_race.models import *

# Create your views here.


def get_completion_percent():
    number_of_made_recipes = Making.objects.values('recipe').distinct().count()
    number_of_recipes = Recipe.objects.count()
    percent = (number_of_made_recipes / number_of_recipes) * 100
    return percent


def index(request):
    """
    main view for home page
    """
    data = \
    {
        'completed_percent': get_completion_percent(),
    }
    return render(request, 'yotams_race/index.html', data)
