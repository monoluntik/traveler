# Generated by Django 4.2.7 on 2023-11-27 06:00

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_alter_outboundstour_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='outboundstour',
            name='inprice_description',
            field=django_quill.fields.QuillField(default='asdf'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outboundstour',
            name='price_kgs',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='outboundstour',
            name='price_usd',
            field=models.FloatField(default=0),
        ),
    ]
