# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-07 20:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180307_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campo',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2018, 3, 7, 20, 27, 0, 235318, tzinfo=utc), verbose_name='Criado em'),
        ),
    ]