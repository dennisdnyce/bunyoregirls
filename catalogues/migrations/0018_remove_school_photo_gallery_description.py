# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-31 20:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogues', '0017_auto_20170831_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school_photo_gallery',
            name='description',
        ),
    ]
