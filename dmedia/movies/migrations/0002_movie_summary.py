# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='summary',
            field=models.CharField(default='N/A', max_length=4096),
            preserve_default=False,
        ),
    ]
