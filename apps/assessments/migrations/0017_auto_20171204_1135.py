# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-04 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0016_auto_20171128_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answergroup_institution',
            name='double_entry',
        ),
        migrations.RemoveField(
            model_name='answergroup_student',
            name='double_entry',
        ),
        migrations.RemoveField(
            model_name='answergroup_studentgroup',
            name='double_entry',
        ),
        migrations.AddField(
            model_name='answerinstitution',
            name='double_entry',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answerstudent',
            name='double_entry',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answerstudentgroup',
            name='double_entry',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='max_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='pass_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='questiongroup',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
