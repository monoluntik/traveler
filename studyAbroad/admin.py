from django.contrib import admin
from studyAbroad.models import StudyAbroad, StudyAbroadForWhome, StudyAbriadAdditional, StudyAbroadImage

class StudyAbroadForWhomeInLine(admin.TabularInline):
    model = StudyAbroadForWhome
    max_num = 50
    min_num = 1

class StudyAbriadAdditionalInLine(admin.TabularInline):
    model = StudyAbriadAdditional
    max_num = 50
    min_num = 1

class StudyAbroadImageInLine(admin.TabularInline):
    model = StudyAbroadImage
    max_num = 50
    min_num = 1


@admin.register(StudyAbroad)
class StudyAbroadAdmin(admin.ModelAdmin):
    inlines = [StudyAbroadForWhomeInLine, StudyAbriadAdditionalInLine, StudyAbroadImageInLine]