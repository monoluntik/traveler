# Generated by Django 4.2.7 on 2023-12-04 08:08

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=255)),
                ('end', models.CharField(max_length=255)),
                ('set_up', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', django_quill.fields.QuillField()),
            ],
        ),
    ]
