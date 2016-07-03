from django import forms

class ConsumedProductForm(forms.Form):
    count = forms.IntegerField()
    date = forms.DateField()
