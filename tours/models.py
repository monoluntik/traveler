from django.db import models
from django_countries.fields import CountryField
# Create your models here.
from django_quill.fields import QuillField

class OutboundsTour(models.Model):
    name = models.CharField(max_length=555)
    description = models.CharField(max_length=555,verbose_name='Описание')
    price_kgs = models.FloatField(default=0, verbose_name='Цена в долларах')
    price_usd = models.FloatField(default=0, verbose_name='Цена в сомах')
    inprice_description = QuillField(verbose_name='Условия тура')
    amount_days = models.IntegerField(verbose_name='Количество дней')
    amount_nights = models.IntegerField(verbose_name='Количество ночей')
    is_last_minute_tours = models.BooleanField(verbose_name='Горящие туры')
    is_sightseeing_tour = models.BooleanField(verbose_name='Экскурсионный тур')
    is_economy_tour = models.BooleanField(verbose_name='Экономичный тур')
    is_romantic_getaways = models.BooleanField(verbose_name='Романтический отдых')
    is_active_leisure = models.BooleanField(verbose_name='Активный отдых')
    is_holiday_tours = models.BooleanField(verbose_name='Туры на праздники')

class OutboundsTourCountry(models.Model):
    country = CountryField()
    outbounds_tour = models.ForeignKey(OutboundsTour, on_delete=models.CASCADE, related_name='countries')
    
class OutboundsTourDay(models.Model):
    number = models.IntegerField()
    description = QuillField()
    outbounds_tour = models.ForeignKey(OutboundsTour, on_delete=models.CASCADE, related_name='days')

class OutboundsTourImage(models.Model):
    image = models.ImageField()
    outbounds_tour = models.ForeignKey(OutboundsTour, on_delete=models.CASCADE, related_name='images')
