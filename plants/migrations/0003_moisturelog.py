# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_auto_20160309_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoistureLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('moisture_level', models.IntegerField(default=0)),
            ],
        ),
    ]