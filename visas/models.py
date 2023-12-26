from django.db import models
from django_quill.fields import QuillField

# Create your models here.


class Visas(models.Model):
    name = models.CharField(max_length=555)
    description = QuillField()

class OpenVisaToGoAbroad(models.Model):
    country = models.CharField(max_length=255)
    description = models.CharField(max_length=555) 

class CountriesToComeFromAbroad(models.Model):
    country = models.CharField(max_length=255)
    description = models.CharField(max_length=555)     

