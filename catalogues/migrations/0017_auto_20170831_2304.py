# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-31 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogues', '0016_auto_20170831_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_performance',
            name='kcse_year',
            field=models.CharField(default='2007', max_length=5),
        ),
    ]
