# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-18 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dise', '0002_auto_20170718_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicdata',
            name='assembly_name',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='basicdata',
            name='parliament_name',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]