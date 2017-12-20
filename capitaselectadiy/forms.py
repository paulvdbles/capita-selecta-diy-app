from django import forms


class LightsForm(forms.Form):
    name = forms.CharField(max_length=100)
    ip = forms.CharField(max_length=100)

