from django.contrib import admin
from work_abroad.models import WorkAbroad, WorkAbroadImage
# Register your models here.
class WorkAbroadImageInLine(admin.TabularInline):
    model = WorkAbroadImage
    max_num = 50
    min_num = 1

@admin.register(WorkAbroad)
class WorkAbroadAdmin(admin.ModelAdmin):
    inlines = [WorkAbroadImageInLine]