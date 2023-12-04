# Generated by Django 4.2.7 on 2023-11-27 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_outboundstourday_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outboundstour',
            name='country',
        ),
        migrations.AddField(
            model_name='outboundstour',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outboundstour',
            name='name',
            field=models.CharField(default=1, max_length=555),
            preserve_default=False,
        ),
    ]
