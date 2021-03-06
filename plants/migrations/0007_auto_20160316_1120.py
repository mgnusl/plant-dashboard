# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0006_auto_20160316_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantcollection',
            name='plants',
        ),
        migrations.RemoveField(
            model_name='plantinstance',
            name='moisture_log',
        ),
        migrations.RemoveField(
            model_name='plantinstance',
            name='watering_log',
        ),
        migrations.AddField(
            model_name='plantinstance',
            name='pin_number',
            field=models.IntegerField(default=0, help_text='Pin number of the humidity sensor'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='ideal_humidity',
            field=models.CharField(help_text='Ideal humidity (LOW, MODERATE, HIGH)', max_length=100),
        ),
        migrations.DeleteModel(
            name='PlantCollection',
        ),
    ]
