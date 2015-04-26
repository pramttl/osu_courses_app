# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbook',
            name='cover_url',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
