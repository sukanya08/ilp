# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boundary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pincode',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
