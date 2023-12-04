from django.contrib import admin
from tours.models import OutboundsTour, OutboundsTourCountry, OutboundsTourDay, OutboundsTourImage
# Register your models here.

class OutboundsTourCountryInLine(admin.TabularInline):
    model = OutboundsTourCountry
    max_num = 50
    min_num = 1

class OutboundsTourDayInLine(admin.TabularInline):
    model = OutboundsTourDay
    max_num = 50
    min_num = 1

class OutboundsTourImageInLine(admin.TabularInline):
    model = OutboundsTourImage
    max_num = 50
    min_num = 1

@admin.register(OutboundsTour)
class OutboundsTourAdmin(admin.ModelAdmin):
    inlines = [OutboundsTourCountryInLine, OutboundsTourDayInLine, OutboundsTourImageInLine]