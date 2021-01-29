

from django.urls import path
from . import views
from django.conf.urls import url
from .views import get_comments


urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^operations/add_new_making/', views.add_new_making, name='add_new_making'),
    url(r'^operations/add_recipe/', views.add_recipe, name='add_recipe'),
    url(r'^operations/add_source/', views.add_source, name='add_source'),
    url(r'^operations/add_making/', views.add_making, name='add_making'),
    url(r'^operations/', views.operations, name='operations'),
    url(r'^recipe_list/', views.recipe_list, name='recipe_list'),
    #url(r'^full_making_table', views.full_making_table, name='full_making_table'),
    url(r'^getRandomRecipe/', views.get_random_recipe, name='getRandomRecipe'),
    url(r'^get_comments/(?P<recipe_id>[0-9]+)$', get_comments, name='get_comments'),
]
