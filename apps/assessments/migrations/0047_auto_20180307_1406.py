# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-07 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0046_auto_20180307_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='image_required',
        ),
        migrations.AddField(
            model_name='questiongroup',
            name='comments_required',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='questiongroup',
            name='image_required',
            field=models.NullBooleanField(default=False),
        ),
    ]