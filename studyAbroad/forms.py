# Ваш файл forms.py
from django import forms
from django_countries.fields import CountryField
from .models import StudyAbroad, CH_type_of_training, CH_language, CH_accommodation, CH_for_whome

class StudyAbroadFilterForm(forms.ModelForm):
    class Meta:
        model = StudyAbroad
        fields = ['country', 'type_of_training', 'language', 'accommodation']


    country = CountryField(blank_label='Страна', default='RU').formfield(required=False)
    type_of_training = forms.ChoiceField(choices=(('', 'Тип программы'),) + CH_type_of_training, required=False)
    language = forms.ChoiceField(choices=(('', 'Язык'),) + CH_language, required=False)
    accommodation = forms.ChoiceField(choices=(('', 'Форма проживания'),) + CH_accommodation, required=False)
    for_whome = forms.ChoiceField(choices=(('', 'Для кого'),)+CH_for_whome, required=False)