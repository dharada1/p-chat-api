# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Tweet(models.Model):
    text = models.CharField(max_length=140)
    user_id = models.IntegerField(default=0)
