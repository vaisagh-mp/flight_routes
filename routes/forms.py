from django import forms
from .models import Airport, AirportRoute

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['name']

class AirportRouteForm(forms.ModelForm):
    class Meta:
        model = AirportRoute
        fields = ['parent', 'child', 'position', 'duration']


class SearchRouteForm(forms.Form):
    start_airport = forms.ModelChoiceField(queryset=Airport.objects.all())
    direction = forms.ChoiceField(
        choices=[('LEFT', 'Left'), ('RIGHT', 'Right')]
    )
