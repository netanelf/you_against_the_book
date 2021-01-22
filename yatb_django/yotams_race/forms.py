from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from bootstrap_modal_forms.forms import BSModalModelForm


class EditMakingForm(BSModalModelForm):
    class Meta:
        timestamp = forms.DateTimeField()
        score = forms.FloatField()
        effort = forms.FloatField()