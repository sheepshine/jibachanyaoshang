# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiderCore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='title', max_length=64),
        ),
    ]
