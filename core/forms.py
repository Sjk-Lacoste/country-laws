from django import forms
from .models import Country


countries = Country.objects.all()

SA = "SA"
B = "B"


COUNTRIES = [
    (SA, "South Africa"),
    (B, "Botswana")
]

class CountriesForm(forms.Form):
    from_country = forms.CharField(label='Where are you from?', widget=forms.Select(choices=COUNTRIES))
    to_country = forms.CharField(label='Country you want to visit?', widget=forms.Select(choices=COUNTRIES))