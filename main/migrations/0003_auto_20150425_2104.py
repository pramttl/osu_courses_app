# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150425_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='end_time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='fri',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='mon',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='start_time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='thu',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='tue',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='wed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(blank=True, to='main.Professor', null=True),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='course',
            field=models.ForeignKey(blank=True, to='main.Course', null=True),
        ),
    ]
