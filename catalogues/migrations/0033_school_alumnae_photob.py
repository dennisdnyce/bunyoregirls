# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-11 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogues', '0032_auto_20170925_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='school_alumnae',
            name='photob',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
