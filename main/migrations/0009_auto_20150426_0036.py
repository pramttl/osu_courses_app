# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150426_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='credits',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
    ]
