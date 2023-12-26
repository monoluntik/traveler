# Ваш файл views.py
from django.views.generic import ListView, DetailView
from .models import Education

class EducationListView(ListView):
    model = Education
    template_name = 'education_list.html'
    context_object_name = 'educations'

class EducationDetailView(DetailView):
    model = Education
    template_name = 'education_detail.html'
    context_object_name = 'education'
