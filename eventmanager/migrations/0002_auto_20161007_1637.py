# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-07 13:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='sum',
            new_name='amount',
        ),
    ]
