from django import forms
from .models import Workers

class TableWorkersForm(forms.Form):
    name = forms.CharField(max_length=50)
    position = forms.CharField(max_length=50)
    working_hours_month = forms.FloatField()
    holiday_this_month = forms.BooleanField()