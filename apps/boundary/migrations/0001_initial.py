# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 06:28
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boundary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('dise_slug', models.CharField(blank=True, max_length=300)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='BoundaryNeighbours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boundary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boundary.Boundary')),
                ('neighbour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boundary_neighbour', to='boundary.Boundary')),
            ],
        ),
        migrations.CreateModel(
            name='BoundaryType',
            fields=[
                ('char_id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ElectionBoundary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dise_slug', models.CharField(blank=True, max_length=300)),
                ('elec_comm_code', models.IntegerField()),
                ('const_ward_name', models.CharField(max_length=300)),
                ('current_elected_rep', models.CharField(blank=True, max_length=300)),
                ('const_ward_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boundary.BoundaryType')),
            ],
        ),
        migrations.CreateModel(
            name='ElectionNeighbours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elect_boundary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boundary.ElectionBoundary')),
                ('neighbour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='electionboundary_neighbour', to='boundary.ElectionBoundary')),
            ],
        ),
        migrations.CreateModel(
            name='ElectionParty',
            fields=[
                ('char_id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='electionparty',
            unique_together=set([('name',)]),
        ),
        migrations.AddField(
            model_name='electionboundary',
            name='current_elected_party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boundary.ElectionParty'),
        ),
        migrations.AddField(
            model_name='electionboundary',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boundary.ElectionBoundary'),
        ),
        migrations.AddField(
            model_name='electionboundary',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Status'),
        ),
        migrations.AddField(
            model_name='boundary',
            name='boundary_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boundary.BoundaryType'),
        ),
        migrations.AddField(
            model_name='boundary',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boundary.Boundary'),
        ),
        migrations.AddField(
            model_name='boundary',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Status'),
        ),
        migrations.AddField(
            model_name='boundary',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.InstitutionType'),
        ),
        migrations.AlterUniqueTogether(
            name='electionneighbours',
            unique_together=set([('elect_boundary', 'neighbour')]),
        ),
        migrations.AlterUniqueTogether(
            name='electionboundary',
            unique_together=set([('elec_comm_code',)]),
        ),
        migrations.AlterUniqueTogether(
            name='boundaryneighbours',
            unique_together=set([('boundary', 'neighbour')]),
        ),
        migrations.AlterUniqueTogether(
            name='boundary',
            unique_together=set([('name', 'parent')]),
        ),
    ]