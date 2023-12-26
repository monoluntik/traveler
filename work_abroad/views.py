from django.shortcuts import render, get_object_or_404
from .models import WorkAbroad

def work_abroad_list(request):
    work_abroads = WorkAbroad.objects.all()
    return render(request, 'work_abroad_list.html', {'work_abroads': work_abroads})

def work_abroad_detail(request, pk):
    work_abroad = get_object_or_404(WorkAbroad, pk=pk)
    return render(request, 'work_abroad_detail.html', {'work_abroad': work_abroad})
