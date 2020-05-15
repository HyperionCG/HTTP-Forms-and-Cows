from django import forms
from say.models import Input

class InputForm(forms.Form):
    text = forms.CharField(max_length=100)