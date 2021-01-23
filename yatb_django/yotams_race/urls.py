

from django.urls import path
from . import views
from django.conf.urls import url
from .views import get_comments


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rate_recipe/', views.rate_recipe, name='rate_recipe'),
    url(r'^making_list/', views.making_list, name='making_list'),
    url(r'^full_making_table', views.full_making_table, name='full_making_table'),
    url(r'^getRandomRecipe/', views.get_random_recipe, name='getRandomRecipe'),
    url(r'^add_new_making/', views.add_new_making, name='addNewMaking'),
    url(r'^get_comments/(?P<recipe_id>[0-9]+)$', get_comments, name='get_comments'),
]