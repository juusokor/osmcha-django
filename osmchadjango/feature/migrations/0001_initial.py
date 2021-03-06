# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-05 12:31
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('changeset', '0029_suspiciousfeature_timestamp'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.IntegerField()),
                ('geometry', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('geojson', django.contrib.postgres.fields.jsonb.JSONField()),
                ('harmful', models.NullBooleanField()),
                ('checked', models.BooleanField(default=False)),
                ('check_date', models.DateTimeField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('changeset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='changeset.Changeset')),
                ('check_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reasons', models.ManyToManyField(related_name='features', to='changeset.SuspicionReasons')),
                ('user_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='changeset.UserDetail')),
            ],
        ),
    ]
