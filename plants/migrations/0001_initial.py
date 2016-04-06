# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-17 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('ideal_humidity', models.DecimalField(decimal_places=2, help_text='Ideal humidity (between 0 and 1', max_digits=3)),
                ('fertilizing_interval', models.IntegerField(blank=True, default=0, help_text='How often the plant needs fertilizer (in days)')),
                ('ideal_ph_min', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Minimum ideal pH value', max_digits=3)),
                ('ideal_ph_max', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Maximum ideal pH value', max_digits=3)),
            ],
        ),
    ]
