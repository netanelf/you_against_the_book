from django.shortcuts import render
from django.db.models import Count, Avg
from django.db.models import Max, Min
from django.http import HttpResponse
from datetime import date, datetime
import json
import random

from yotams_race.models import *

# Create your views here.


def get_completion_data():
    number_of_made_recipes = Making.objects.values('recipe').distinct().count()
    number_of_recipes = Recipe.objects.count()
    percent = (number_of_made_recipes / number_of_recipes) * 100
    data = {'percent': percent, 'number_of_recipes': number_of_recipes, 'number_of_made_recipes': number_of_made_recipes}
    return data


def get_top_10_recipes():
    makings = Recipe.objects.annotate(num_makings=Count('making'),
                                      avg_rank=Avg('making__score'),
                                      avg_effort=Avg('making__effort')).order_by('-num_makings', '-avg_rank', '-avg_effort')
    top_10 = makings[:10]
    data = [{'name': v.name,
             'num_makings': v.num_makings,
             'average_rank': v.avg_rank,
             'average_effort': v.avg_effort} for v in top_10]
    return data


def get_full_recipes_list():
    recipes = Recipe.objects.all()
    l = [r.name for r in recipes]
    return l


def index(request):
    """
    main view for home page
    """
    data = \
    {
        'completed_percent': get_completion_data(),
        'top_10': get_top_10_recipes(),
        'full_recipes_list': get_full_recipes_list(),
        'todays_date': date.today().strftime('%Y-%m-%d')
    }
    return render(request, 'yotams_race/index.html', data)


def get_random_recipe(request):

    a = request.GET.keys()
    k = list(a)[0]
    data = json.loads(k)
    only_not_made = data[1]
    max_id = Recipe.objects.all().aggregate(max_id=Max("id"))['max_id']
    min_id = Recipe.objects.all().aggregate(min_id=Min("id"))['min_id']
    found_rand_recipe = False
    while not found_rand_recipe:
        pk = random.randint(min_id, max_id)
        random_recipe = Recipe.objects.get(pk=pk)
        if not only_not_made:
            found_rand_recipe = True
        else:
            if len(random_recipe.making_set.all()) == 0:
                found_rand_recipe = True
            else:
                print(f'recipe {random_recipe.name} was already made, choosing another one')

    data = {'name': random_recipe.name,
            'page': random_recipe.page_num}
    return HttpResponse(json.dumps(data))


def add_new_making(request):
    print(request)
    a = request.GET.keys()
    k = list(a)[0]
    data = json.loads(k)
    print(f'{k}')
    r = Recipe.objects.get(name=data[0])
    timestamp = datetime.strptime(data[1] + ' 12:00:00', '%Y-%m-%d %H:%M:%S')
    score = float(data[2])
    effort = float(data[3])
    making = Making(recipe=r, timestamp=timestamp, score=score, effort=effort)
    making.save()
    return HttpResponse(json.dumps({'no_data': None}))

