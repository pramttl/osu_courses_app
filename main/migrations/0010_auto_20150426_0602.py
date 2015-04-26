# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150426_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textbook',
            name='course',
        ),
        migrations.AddField(
            model_name='textbook',
            name='amazon_price',
            field=models.CharField(max_length=16, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='textbook',
            name='osu_price',
            field=models.CharField(max_length=16, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='textbook',
            name='textbook_class',
            field=models.ForeignKey(blank=True, to='main.Class', null=True),
        ),
    ]
