# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150425_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='name',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
