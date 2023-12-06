from django.shortcuts import render
from tours.models import OutboundsTour
from studyAbroad.models import StudyAbroad
from visas.models import Visas
from work_abroad.models import WorkAbroad 
# Create your views here.




'main short lists of all --- request'
'tours list pk -- listview detailview'
'study abroad list pk -- listview detailview'
'academy list pk -- listview detailview'
'visa list pk -- listview detailview'
'work abroad list pk -- listview detailview'

def showAllShortsLists(request):
    outboundsToursAll = OutboundsTour.objects.all()
    studyAbroad = StudyAbroad.objects.all()
    visas = Visas.objects.all()
    workAbroad = WorkAbroad.objects.all()
    if outboundsToursAll.count() >= 5:
        outbounds_tours_first_5 = outboundsToursAll[:5]
    else:
        # Handle the case where there are fewer than 5 objects
        outbounds_tours_first_5 = outboundsToursAll

    if studyAbroad.count() >= 5:
        studyAbroad_first_5 = studyAbroad[:5]
    else:
        # Handle the case where there are fewer than 5 objects
        studyAbroad_first_5 = studyAbroad

    if visas.count() >= 5:
        visas_first_5 = visas[:5]
    else:
        # Handle the case where there are fewer than 5 objects
        visas_first_5 = visas

    if workAbroad.count() >= 5:
        workAbroadfirst_5 = workAbroad[:5]
    else:
        # Handle the case where there are fewer than 5 objects
        workAbroad = workAbroad


    return render(
        request, "index.html", 
        {
            "outboundsToursAll": outbounds_tours_first_5, 
            "studyAbroad": studyAbroad_first_5, 
            "visas": visas_first_5, 
            'work_abroads': workAbroad, 
        }
    )




from django.shortcuts import render
from tours.models import OutboundsTour
from tours.forms import OutboundTourForm

def outbound_tour_view(request):
    if request.method == 'POST':
        form = OutboundTourForm(request.POST)
        if form.is_valid():
            # Получение валидированных данных из формы
            is_last_minute_tours = form.cleaned_data.get('is_last_minute_tours', False)
            is_sightseeing_tour = form.cleaned_data.get('is_sightseeing_tour', False)
            is_economy_tour = form.cleaned_data.get('is_economy_tour', False)
            is_romantic_getaways = form.cleaned_data.get('is_romantic_getaways', False)
            is_active_leisure = form.cleaned_data.get('is_active_leisure', False)
            is_holiday_tours = form.cleaned_data.get('is_holiday_tours', False)
            country = form.cleaned_data.get('country', None)
            # Фильтрация данных
            queryset = OutboundsTour.objects.all()

            # Применение фильтров
            if is_last_minute_tours:
                queryset = queryset.filter(is_last_minute_tours=True)

            if is_sightseeing_tour:
                queryset = queryset.filter(is_sightseeing_tour=True)

            if is_economy_tour:
                queryset = queryset.filter(is_economy_tour=True)

            if is_romantic_getaways:
                queryset = queryset.filter(is_romantic_getaways=True)

            if is_active_leisure:
                queryset = queryset.filter(is_active_leisure=True)

            if is_holiday_tours:
                queryset = queryset.filter(is_holiday_tours=True)

            if country:
                queryset = queryset.filter(countries__country=country)

            
            return render(request, 'outboundstour_list.html', {'form': form, 'outboundsToursAll': queryset})
    else:
        form = OutboundTourForm()

    return render(request, 'outboundstour_list.html', {'form': form, 'outboundsToursAll': OutboundsTour.objects.all()})


# Ваш файл views.py
from django.shortcuts import render, get_object_or_404
from .models import OutboundsTour

def outbound_tour_detail_view(request, tour_id):
    tour = get_object_or_404(OutboundsTour, id=tour_id)
    print(tour.images.all)
    return render(request, 'tour_detail.html', {'tour': tour})
