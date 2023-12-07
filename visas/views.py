from django.shortcuts import render, get_object_or_404
from .models import Visas, OpenVisaToGoAbroad, CountriesToComeFromAbroad

def visas_list(request):
    visas = Visas.objects.all()
    open_visas = OpenVisaToGoAbroad.objects.all()
    countries_to_come = CountriesToComeFromAbroad.objects.all()
    return render(request, 'visas_list.html', {'visas': visas, 'open_visas': open_visas, 'countries_to_come': countries_to_come})

def visas_detail(request, pk):
    visa = get_object_or_404(Visas, pk=pk)
    return render(request, 'visas_detail.html', {'visa': visa})


