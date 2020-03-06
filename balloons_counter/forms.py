from django import forms
from django.core.validators import MinValueValidator

from balloons_counter.models import Entity
import balloons_counter.constants as const


class ExampleForm(forms.Form):
    weight = forms.IntegerField(validators=[MinValueValidator(1)])
    measure = forms.ChoiceField(choices=const.MEASURES, initial=const.DEFAULT_MEASURE)
    # username = forms.CharField(max_length=75)
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
