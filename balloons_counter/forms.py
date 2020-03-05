from django import forms
from django.core.validators import MinValueValidator


class RegistrationForm(forms.Form):
    weight = forms.IntegerField(validators=[MinValueValidator(1)])
    measure = forms.CharField()
    # username = forms.CharField(max_length=75)
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
