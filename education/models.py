from django.db import models
from django_quill.fields import QuillField

# Create your models here.


class Education(models.Model):
    start = models.CharField(max_length=255)
    end = models.CharField(max_length=255)
    set_up = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = QuillField()