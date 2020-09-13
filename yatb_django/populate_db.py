from csv import DictReader
from datetime import datetime, timezone
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatb_django.settings')
import django
django.setup()
from yotams_race.models import Recipe, Making


RECIPES_FILE_PATH = r'/home/netanel/workspace/you_against_the_book/yatb_django/recipes.csv'


def populate_recipes():
    with open(RECIPES_FILE_PATH, 'r') as f:
        reader = DictReader(f)
        for l in reader:
            print(f'found line: {l}')
            r = Recipe(name=l['recipe_name'],
                       page_num=l['page_number'])
            r.save()


def populate_makings():
    r = Recipe.objects.all()[0]
    m = Making(
        recipe=r,
        timestamp=datetime.now(tz=timezone.utc),
        score=2
    )
    m.save()


if __name__ == '__main__':
    populate_recipes()
    populate_makings()
