# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 05:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogues', '0027_auto_20170915_0538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form_four_news_portal',
            name='author',
        ),
        migrations.RemoveField(
            model_name='form_one_news_portal',
            name='author',
        ),
        migrations.RemoveField(
            model_name='form_three_news_portal',
            name='author',
        ),
        migrations.RemoveField(
            model_name='form_two_news_portal',
            name='author',
        ),
        migrations.RemoveField(
            model_name='school_admission',
            name='author',
        ),
        migrations.RemoveField(
            model_name='school_documents_downloads',
            name='author',
        ),
        migrations.RemoveField(
            model_name='school_rules',
            name='author',
        ),
        migrations.DeleteModel(
            name='Form_four_news_portal',
        ),
        migrations.DeleteModel(
            name='Form_one_news_portal',
        ),
        migrations.DeleteModel(
            name='Form_three_news_portal',
        ),
        migrations.DeleteModel(
            name='Form_two_news_portal',
        ),
        migrations.DeleteModel(
            name='School_admission',
        ),
        migrations.DeleteModel(
            name='School_documents_downloads',
        ),
        migrations.DeleteModel(
            name='School_rules',
        ),
    ]