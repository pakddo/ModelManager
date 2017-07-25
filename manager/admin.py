# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Model, Project

admin.site.register(Model)
admin.site.register(Project)
