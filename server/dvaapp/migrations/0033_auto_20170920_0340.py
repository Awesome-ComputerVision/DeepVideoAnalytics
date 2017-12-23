# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 03:40
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0032_queryregionresults'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyzer',
            name='additional_files',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='analyzer',
            name='url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='analyzer',
            name='mode',
            field=models.CharField(choices=[('T', 'Tensorflow'), ('C', 'Caffe'), ('P', 'Pytorch'), ('O', 'OpenCV'), ('M', 'MXNet')], db_index=True, default='T', max_length=1),
        ),
        migrations.AlterField(
            model_name='detector',
            name='mode',
            field=models.CharField(choices=[('T', 'Tensorflow'), ('C', 'Caffe'), ('P', 'Pytorch'), ('O', 'OpenCV'), ('M', 'MXNet')], db_index=True, default='T', max_length=1),
        ),
        migrations.AlterField(
            model_name='indexer',
            name='mode',
            field=models.CharField(choices=[('T', 'Tensorflow'), ('C', 'Caffe'), ('P', 'Pytorch'), ('O', 'OpenCV'), ('M', 'MXNet')], db_index=True, default='T', max_length=1),
        ),
    ]