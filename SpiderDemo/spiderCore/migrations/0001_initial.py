# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=32)),
                ('content', models.TextField(null=True)),
                ('url', models.TextField(null=True)),
            ],
        ),
    ]
