"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tours.views import showAllShortsLists, outbound_tour_view, outbound_tour_detail_view
from studyAbroad.views import study_abroad_list, study_abroad_detail
from django.conf import settings
from django.conf.urls.static import static
from work_abroad.views import work_abroad_list, work_abroad_detail
from visas.views import visas_list, visas_detail
from education.views import EducationDetailView, EducationListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', showAllShortsLists, name='home'),
    path('outbounds-tours/', outbound_tour_view, name='outbounds-tours-name'),
    path('study-abroad/', study_abroad_list, name='study-abroad-list'),
    path('study-abroad/<int:pk>/', study_abroad_detail, name='study-abroad-detail'),
    path('outbounds-tours/<int:tour_id>/', outbound_tour_detail_view, name='outbounds-tours-detail'),
    path('work-abroad/', work_abroad_list, name='work_abroad_list'),
    path('work-abroad/<int:pk>/', work_abroad_detail, name='work_abroad_detail'),
    path('visas/', visas_list, name='visas_list'),
    path('visas/<int:pk>/', visas_detail, name='visas_detail'),
    path('educations/', EducationListView.as_view(), name='education_list'),
    path('educations/<int:pk>/',EducationDetailView.as_view(), name='education_detail'),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




