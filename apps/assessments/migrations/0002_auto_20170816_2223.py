# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-16 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questiongroup',
            name='updated_at',
            field=models.DateField(max_length=20, null=True),
        ),
    ]