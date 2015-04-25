# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150425_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_num',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='major',
            field=models.ForeignKey(blank=True, to='main.Major', null=True),
        ),
        migrations.AddField(
            model_name='major',
            name='abbrv',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
    ]
