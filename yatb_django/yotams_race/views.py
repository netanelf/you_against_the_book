from django.shortcuts import render
from django.db.models import Count, Avg
from django.db.models import Max, Min
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from datetime import date, datetime
import json
import random

from yotams_race.models import *
from yotams_race.forms import RecipeForm, SourceForm, MakingForm

# Create your views here.


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('operations'))

    else:
        form = RecipeForm()

    return render(request, 'yotams_race/add_recipe.html', {'form': form})


def add_source(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('operations'))

    else:
        form = SourceForm()

    return render(request, 'yotams_race/add_source.html', {'form': form})


def add_making(request):
    if request.method == 'POST':
        form = MakingForm(request.POST)
        if form.is_valid():
            r = Recipe.objects.get(pk=form.data['recipe'])
            c = Comment(recipe=r, timestamp=form.data['timestamp'], comment=form.data['comment'])
            c.save()
            form.save()
            return HttpResponseRedirect(reverse('operations'))
        else:
            print(f'form not valid!, form: {form}')
    else:
        form = MakingForm()
    return render(request, 'yotams_race/add_making.html', {'form': form,
                                                           'full_recipes_list': get_full_recipes_list(),
                                                           'todays_date': date.today().strftime('%Y-%m-%d')
                                                           })


def get_comments(request, recipe_id):
    r = Recipe.objects.get(pk=recipe_id)
    comments = Comment.objects.filter(recipe=r)
    data = dict()
    data['recipe_name'] = r.name
    data['comments'] = comments
    return render(request, 'yotams_race/comment_list.html', data)


def get_completion_data():
    plenty_source = Source.objects.get(name='Yotam Ottolenghi, Plenty')
    number_of_made_recipes = Making.objects.values('recipe').filter(recipe__recipe_source=plenty_source).values('recipe').distinct().count()
    number_of_recipes = Recipe.objects.filter(recipe_source=plenty_source).count()
    percent = (number_of_made_recipes / number_of_recipes) * 100
    data = {'percent': percent, 'number_of_recipes': number_of_recipes, 'number_of_made_recipes': number_of_made_recipes}
    return data


def get_top_10_recipes():
    makings = Recipe.objects.annotate(num_makings=Count('making'),
                                      avg_rank=Avg('making__score'),
                                      avg_effort=Avg('making__effort'),
                                      ).order_by('-num_makings', '-avg_rank', '-avg_effort')
    top_10 = makings[:10]
    data = [{'name': v.name,
             'num_makings': v.num_makings,
             'average_rank': v.avg_rank,
             'average_effort': v.avg_effort,
             'id': v.id} for v in top_10]
    return data


def get_full_recipes_list():
    recipes = Recipe.objects.all()
    l = [{'name': r.name, 'id': r.id} for r in recipes]
    return l


def index(request):
    """
    main view for home page
    """
    print('index view')
    data = \
    {
        'completed_percent': get_completion_data(),
        'top_10': get_top_10_recipes(),
        'todays_date': date.today().strftime('%Y-%m-%d')
    }
    return render(request, 'yotams_race/index.html', data)


def operations(request):
    print('in operations')
    data = \
        {
            'todays_date': date.today().strftime('%Y-%m-%d')
        }
    return render(request, 'yotams_race/operations.html', data)


def recipe_list(request):
    recipes = Recipe.objects.all()
    recipe_list = []
    for r in recipes:
        recipe_list.append(
            {
                'name': r.name,
                'source': r.recipe_source,
                'page': r.page_num,
                'link': r.link,
                'num_of_comments': Comment.objects.filter(recipe=r).count(),
                'num_of_making': r.making_set.count(),
                'id': r.id
            }
        )
    data = \
        {
            'all_recipes': recipe_list
        }
    return render(request, 'yotams_race/recipe_list.html', data)


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

    try:
        makings = Recipe.objects\
        .filter(name=random_recipe.name)\
        .annotate(num_makings=Count('making'), avg_rank=Avg('making__score'), avg_effort=Avg('making__effort'))
        avg_rank = makings[0].avg_rank
        avg_effort = makings[0].avg_effort
    except Exception as ex:
        avg_rank = 'NA'
        avg_effort = 'NA'

    data = {'name': random_recipe.name,
            'page': random_recipe.page_num,
            'rank': avg_rank,
            'effort': avg_effort}
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
    comment = data[4]
    print(f'comment: {comment}')
    making = Making(recipe=r, timestamp=timestamp, score=score, effort=effort)
    making.save()
    if comment != '':
        comment = Comment(timestamp=timestamp, recipe=r, comment=comment)
        comment.save()
    return HttpResponse(json.dumps({'no_data': None}))

