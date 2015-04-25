# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, null=True, blank=True)),
                ('isbn', models.CharField(max_length=16, null=True, blank=True)),
                ('course', models.ForeignKey(to='main.Course')),
            ],
        ),
        migrations.RenameField(
            model_name='professor',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='rating',
        ),
        migrations.AddField(
            model_name='professor',
            name='last_name',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
    ]
