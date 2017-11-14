# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'content')

admin.site.register(models.Article, ArticleAdmin)
