# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 06:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boundary', '0017_auto_20180214_1024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boundary',
            options={'ordering': ['name'], 'permissions': (('add_institution', 'Add Institution'),)},
        ),
    ]