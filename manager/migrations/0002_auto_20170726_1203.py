# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 03:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='description',
            new_name='text',
        ),
    ]
