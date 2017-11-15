# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.TextField(default='title')
    content = models.TextField(null=True)
    url = models.TextField(null=True)


    def __unicode__(self):
        return self.title
