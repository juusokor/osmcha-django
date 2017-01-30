# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-17 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changeset', '0029_suspiciousfeature_timestamp'),
        ('feature', '0002_remove_feature_osm_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='osm_id',
            field=models.IntegerField(default=1234),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feature',
            name='osm_type',
            field=models.CharField(default='way', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feature',
            name='osm_version',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feature',
            name='url',
            field=models.SlugField(default='way-1234', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='feature',
            unique_together=set([('changeset', 'osm_id', 'osm_type')]),
        ),
    ]