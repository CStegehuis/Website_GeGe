# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-25 01:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20170525_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='source',
        ),
    ]