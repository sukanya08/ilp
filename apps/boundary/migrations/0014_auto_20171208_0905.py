# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-08 03:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boundary', '0013_basicboundaryagg_boundaryinstitutiongenderagg_boundaryschoolcategoryagg_boundaryschoolmanagementagg_'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='boundarystudentmothertongueagg',
            table='mvw_boundary_student_mt_agg',
        ),
    ]