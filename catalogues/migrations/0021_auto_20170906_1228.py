# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 09:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogues', '0020_auto_20170905_1034'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='School_chemistry_department',
            new_name='School_humanities_department',
        ),
        migrations.RenameModel(
            old_name='School_kiswahili_department',
            new_name='School_languages_department',
        ),
        migrations.RenameModel(
            old_name='School_physics_department',
            new_name='School_sciences_department',
        ),
        migrations.RenameModel(
            old_name='School_business_studies_department',
            new_name='School_technicals_department',
        ),
        migrations.RemoveField(
            model_name='school_agriculture_department',
            name='author',
        ),
        migrations.RemoveField(
            model_name='school_biology_department',
            name='author',
        ),
        migrations.RemoveField(
            model_name='school_computer_studies_department',
            name='author',
        ),
        migrations.RemoveField(
            model_name='school_cre_department',
            name='author',
        ),
        migrations.RemoveField(
            model_name='school_english_department',
            name='author',
        ),
        migrations.RemoveField(
            model_name='school_foreignlanguages_department',
            name='author',
        ),
        migrations.RemoveField(
            model_name='school_geography_department',
            name='author',
        ),
        migrations.RemoveField(
            model_name='school_history_department',
            name='author',
        ),
        migrations.RemoveField(
            model_name='school_homescience_department',
            name='author',
        ),
        migrations.DeleteModel(
            name='School_agriculture_department',
        ),
        migrations.DeleteModel(
            name='School_biology_department',
        ),
        migrations.DeleteModel(
            name='School_computer_studies_department',
        ),
        migrations.DeleteModel(
            name='School_cre_department',
        ),
        migrations.DeleteModel(
            name='School_english_department',
        ),
        migrations.DeleteModel(
            name='School_foreignlanguages_department',
        ),
        migrations.DeleteModel(
            name='School_geography_department',
        ),
        migrations.DeleteModel(
            name='School_history_department',
        ),
        migrations.DeleteModel(
            name='School_homescience_department',
        ),
    ]
