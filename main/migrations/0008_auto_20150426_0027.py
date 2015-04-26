# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crn', models.CharField(max_length=16, null=True, blank=True)),
                ('term', models.CharField(max_length=8, null=True, blank=True)),
                ('mon', models.BooleanField(default=False)),
                ('tue', models.BooleanField(default=False)),
                ('wed', models.BooleanField(default=False)),
                ('thu', models.BooleanField(default=False)),
                ('fri', models.BooleanField(default=False)),
                ('start_time', models.TimeField(null=True, blank=True)),
                ('end_time', models.TimeField(null=True, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('loc', models.CharField(max_length=32, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='crn',
        ),
        migrations.RemoveField(
            model_name='course',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='course',
            name='fri',
        ),
        migrations.RemoveField(
            model_name='course',
            name='loc',
        ),
        migrations.RemoveField(
            model_name='course',
            name='mon',
        ),
        migrations.RemoveField(
            model_name='course',
            name='professor',
        ),
        migrations.RemoveField(
            model_name='course',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='course',
            name='term',
        ),
        migrations.RemoveField(
            model_name='course',
            name='thu',
        ),
        migrations.RemoveField(
            model_name='course',
            name='tue',
        ),
        migrations.RemoveField(
            model_name='course',
            name='wed',
        ),
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='class',
            name='course',
            field=models.ForeignKey(to='main.Course'),
        ),
        migrations.AddField(
            model_name='class',
            name='professor',
            field=models.ForeignKey(blank=True, to='main.Professor', null=True),
        ),
    ]
