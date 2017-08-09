# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Project(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


class Model(models.Model):
    project = models.ForeignKey(Project)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    epoch = models.IntegerField(default=0)
    trainig_data_count = models.IntegerField(default=0)
    accuracy = models.FloatField(default=0.0)
    created_date = models.DateTimeField(default=timezone.now)
    trained_date = models.DateTimeField(blank=True, null=True)
