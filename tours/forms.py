# forms.py
from django import forms
from django_countries.fields import CountryField

class OutboundTourForm(forms.Form):
    country = CountryField(blank_label='Страна', default='RU').formfield(required=False)
    is_last_minute_tours = forms.BooleanField(required=False)
    is_sightseeing_tour = forms.BooleanField(required=False)
    is_economy_tour = forms.BooleanField(required=False)
    is_romantic_getaways = forms.BooleanField(required=False)
    is_active_leisure = forms.BooleanField(required=False)
    is_holiday_tours = forms.BooleanField(required=False)
