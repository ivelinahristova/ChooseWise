from django import forms
from .models import Foods
from .models import Nutrients

class ConsumedProductForm(forms.Form):
    foods = forms.ModelChoiceField(queryset=Foods.objects.all().order_by('name'))
    count = forms.IntegerField()
    date = forms.DateField()

class DietForm(forms.Form):
    nutrient = forms.ModelChoiceField(queryset=Nutrients.objects.all().order_by('name'))
    grams = forms.IntegerField()
