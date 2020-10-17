

from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^full_making_table', views.full_making_table, name='full_making_table'),
    url(r'^getRandomRecipe/', views.get_random_recipe, name='getRandomRecipe'),
    url(r'^add_new_making/', views.add_new_making, name='addNewMaking'),
]