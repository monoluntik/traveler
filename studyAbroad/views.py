# Ваш файл views.py
from django.shortcuts import render
from .forms import StudyAbroadFilterForm
from .models import StudyAbroad

# def study_abroad_list(request):
#     form = StudyAbroadFilterForm(request.GET)
#     studies = StudyAbroad.objects.all()
 
#     if form.is_valid():
#         country = form.cleaned_data.get('country')
#         type_of_training = form.cleaned_data.get('type_of_training')
#         language = form.cleaned_data.get('language')
#         accommodation = form.cleaned_data.get('accommodation')

#         if country:
#             studies = studies.filter(country=country)
#         if type_of_training:
#             studies = studies.filter(type_of_training=type_of_training)
#         if language:
#             studies = studies.filter(language=language)
#         if accommodation:
#             studies = studies.filter(accommodation=accommodation)

#     context = {'form': form, 'studies': studies}
#     return render(request, 'study_abroad_list.html', context)

from django.shortcuts import render, get_object_or_404
from .models import StudyAbroad

def study_abroad_detail(request, pk):
    study = get_object_or_404(StudyAbroad, pk=pk)
    return render(request, 'study_abroad_detail.html', {'study': study})


def study_abroad_list(request):
    if request.method == 'POST':
        form = StudyAbroadFilterForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data.get('country')
            type_of_training = form.cleaned_data.get('type_of_training')
            language = form.cleaned_data.get('language')
            accommodation = form.cleaned_data.get('accommodation')
            for_whome = form.cleaned_data.get('for_whome')
            # Фильтрация данных
            studies = StudyAbroad.objects.all()

       

            if country:
                studies = studies.filter(country=country)
            if type_of_training:
                studies = studies.filter(type_of_training=type_of_training)
            if language:
                studies = studies.filter(language=language)
            if accommodation:
                studies = studies.filter(accommodation=accommodation)
            if for_whome:
                studies = studies.filter(for_whomes__for_whome=for_whome)


            return render(request, 'study_abroad_list.html', {'form': form, 'studies': studies})
    else:
        form = StudyAbroadFilterForm()

    return render(request, 'study_abroad_list.html', {'form': form, 'studies': StudyAbroad.objects.all()})
