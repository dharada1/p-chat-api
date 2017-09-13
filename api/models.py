# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class DummyUser(models.Model):
    name = models.CharField(max_length=50)
    gender = models.IntegerField(default=0) #Mなら1 Fなら2
    #age追加する
    #image追加する(DB保存でいいのか？)
    job = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

class Message(models.Model):
    user = models.ForeignKey(DummyUser, related_name='user', null=True)
    partner = models.ForeignKey(DummyUser, related_name='partner', null=True)
    from_me = models.IntegerField(default=0)
    #user_idがいいね！送信元の場合、from_meは1
    #partner_idがいいね！送信先の場合、from_meは2
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
