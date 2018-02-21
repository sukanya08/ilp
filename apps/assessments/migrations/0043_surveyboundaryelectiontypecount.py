# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-21 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0042_auto_20180217_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyBoundaryElectionTypeCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearmonth', models.IntegerField(db_column='yearmonth')),
                ('electionboundary_count', models.IntegerField(db_column='electionboundary_count')),
            ],
            options={
                'managed': False,
                'db_table': 'mvw_survey_boundary_electiontype_count',
            },
        ),
    ]