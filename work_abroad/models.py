from django.db import models
from django_countries.fields import CountryField
from django_quill.fields import QuillField

# Create your models here.


class WorkAbroad(models.Model):
    country = CountryField()
    name = models.CharField(max_length=255)
    description = QuillField()
    salery_min = models.FloatField(default=0)
    salery_max = models.FloatField(default=0)

class WorkAbroadImage(models.Model):
    work_abroad = models.ForeignKey(WorkAbroad, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()