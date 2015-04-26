# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150426_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='lat',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='class',
            name='lon',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
    ]
