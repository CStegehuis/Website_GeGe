# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-25 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_blogpage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='publish_date',
            field=models.DateField(blank=True, default=-1980, verbose_name=b'Published date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpage',
            name='source',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
