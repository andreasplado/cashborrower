# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-07 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanager', '0002_auto_20161007_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='creditcount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='loan',
            name='discreditcount',
            field=models.IntegerField(default=0),
        ),
    ]