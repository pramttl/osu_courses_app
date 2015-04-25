# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crn', models.CharField(max_length=16, null=True, blank=True)),
                ('name', models.CharField(max_length=32, null=True, blank=True)),
                ('term', models.CharField(max_length=8, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, null=True, blank=True)),
                ('rating', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(to='main.Professor'),
        ),
    ]
