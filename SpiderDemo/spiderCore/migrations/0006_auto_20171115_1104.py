# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiderCore', '0005_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.TextField(default='title'),
        ),
    ]
