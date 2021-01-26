

from django.urls import path
from . import views
from django.conf.urls import url
from .views import get_comments


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rate_recipe/add_new_making/', views.add_new_making, name='addNewMaking'),
    url(r'^rate_recipe/', views.rate_recipe, name='rate_recipe'),
    url(r'^recipe_list/', views.recipe_list, name='recipe_list'),
    #url(r'^full_making_table', views.full_making_table, name='full_making_table'),
    url(r'^getRandomRecipe/', views.get_random_recipe, name='getRandomRecipe'),
    url(r'^get_comments/(?P<recipe_id>[0-9]+)$', get_comments, name='get_comments'),
]
