from csv import DictReader
from datetime import datetime, timezone
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatb_django.settings')
import django
django.setup()
from yotams_race.models import Recipe, Making


RECIPES_FILE_PATH = r'recipes.csv'


def populate_recipes():
    with open(RECIPES_FILE_PATH, 'r') as f:
        reader = DictReader(f, delimiter='|')
        for l in reader:
            print(f'found line: {l}')
            r = Recipe(name=l['recipe_name'],
                       page_num=int(l['page_number']))
            r.save()


def populate_makings():
    r = Recipe.objects.get(name='Soba noodles with aubergine and mango')
    m = Making(
        recipe=r,
        timestamp=datetime(2015,11,3,12,0,0),
        score=4.5
    )
    m.save()

    r = Recipe.objects.get(name='Soba noodles with aubergine and mango')
    m = Making(
        recipe=r,
        timestamp=datetime(2016,11,3,12,0,0),
        score=4.2
    )
    m.save()

    r = Recipe.objects.get(name='Green gazpacho')
    m = Making(
        recipe=r,
        timestamp=datetime(2020,9,10,12,0,0),
        score=4.6
    )
    m.save()

    r = Recipe.objects.get(name='Cucumber salad with smashed garlic and ginger')
    m = Making(
        recipe=r,
        timestamp=datetime(2020,8,20,12,0,0),
        score=4
    )
    m.save()

    r = Recipe.objects.get(name='Mee goreng')
    m = Making(
        recipe=r,
        timestamp=datetime(2019,8,20,12,0,0),
        score=4.3
    )
    m.save()

    r = Recipe.objects.get(name='Broad bean burgers')
    m = Making(
        recipe=r,
        timestamp=datetime(2018,8,20,12,0,0),
        score=3.8
    )
    m.save()

    r = Recipe.objects.get(name='Fried butterbeans with feta, sorrel and sumac')
    m = Making(
        recipe=r,
        timestamp=datetime(2020,5,1,12,0,0),
        score=3.5
    )
    m.save()

    r = Recipe.objects.get(name='Coconut rice with sambal and okra')
    m = Making(
        recipe=r,
        timestamp=datetime(2019,5,1,12,0,0),
        score=4.8
    )
    m.save()


    r = Recipe.objects.get(name='Farro and roasted pepper salad')
    m = Making(
        recipe=r,
        timestamp=datetime(2020,8,1,12,0,0),
        score=4.6
    )
    m.save()


    r = Recipe.objects.get(name='Sweetcorn polenta')
    m = Making(
        recipe=r,
        timestamp=datetime(2020,8,10,12,0,0),
        score=4.2
    )
    m.save()


    r = Recipe.objects.get(name='Sweetcorn polenta')
    m = Making(
        recipe=r,
        timestamp=datetime(2019,6,10,12,0,0),
        score=4.4
    )
    m.save()


    r = Recipe.objects.get(name='Gado-gado')
    m = Making(
        recipe=r,
        timestamp=datetime(2020,10,28,12,0,0),
        score=4.3
    )
    m.save()


def clear_db():
    Making.objects.all().delete()
    Recipe.objects.all().delete()


if __name__ == '__main__':
    clear_db()
    populate_recipes()
    populate_makings()
