# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-11 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0030_surveyboundaryquestiongroupansagg_surveyinstitutionquestiongroupansagg_surveyquestiongroupansagg_sur'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyQuestionGroupInfoAgg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(db_column='year')),
                ('month', models.IntegerField(db_column='month')),
                ('num_schools', models.IntegerField(db_column='num_schools')),
                ('num_assessments', models.IntegerField(db_column='num_assessments')),
                ('num_children', models.IntegerField(db_column='num_children')),
                ('num_users', models.IntegerField(db_column='num_users')),
                ('last_assessment', models.DateField(db_column='last_assessment')),
            ],
            options={
                'managed': False,
                'db_table': 'mvw_survey_questiongroup_info_agg',
            },
        ),
    ]