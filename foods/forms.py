from django import forms
from .models import Foods

class ConsumedProductForm(forms.Form):
    foods = forms.ModelChoiceField(queryset=Foods.objects.all().order_by('name'))
    count = forms.IntegerField()
    date = forms.DateField()
