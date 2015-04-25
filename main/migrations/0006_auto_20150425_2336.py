# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150425_2206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='major',
            old_name='abbrv',
            new_name='abbr',
        ),
        migrations.AlterField(
            model_name='course',
            name='course_num',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
    ]
