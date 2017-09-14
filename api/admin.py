# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import DummyUser, Message

admin.site.register(DummyUser)
admin.site.register(Message)
