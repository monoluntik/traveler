from django.contrib import admin

# Register your models here.
from visas.models import Visas, CountriesToComeFromAbroad, OpenVisaToGoAbroad

admin.site.register(Visas)