
from django import forms
from yotams_race.models import Recipe, Source, Making
from django.forms import CharField, HiddenInput


def get_choices():
    return ('123', '3456')


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = '__all__'


class MakingForm(forms.ModelForm):

    comment = CharField(widget=HiddenInput())

    class Meta:
        model = Making
        fields = '__all__'
