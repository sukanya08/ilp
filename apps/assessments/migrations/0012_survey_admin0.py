# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-16 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boundary', '0012_auto_20170904_1212'),
        ('assessments', '0011_auto_20171011_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='admin0',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='boundary.Boundary'),
            preserve_default=False,
        ),
    ]
