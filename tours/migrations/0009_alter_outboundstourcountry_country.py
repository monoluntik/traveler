# Generated by Django 5.0 on 2023-12-26 10:34

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0008_alter_outboundstour_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outboundstourcountry',
            name='country',
            field=django_countries.fields.CountryField(default='RU', max_length=2),
        ),
    ]
