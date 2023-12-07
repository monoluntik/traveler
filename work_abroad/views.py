from django.shortcuts import render, get_object_or_404
from .models import WorkAbroad
from django.views.decorators.cache import cache_page


@cache_page(60 * 15) 
def work_abroad_list(request):
    work_abroads = WorkAbroad.objects.all()
    return render(request, 'work_abroad_list.html', {'work_abroads': work_abroads})


@cache_page(60 * 15) 
def work_abroad_detail(request, pk):
    work_abroad = get_object_or_404(WorkAbroad, pk=pk)
    return render(request, 'work_abroad_detail.html', {'work_abroad': work_abroad})
