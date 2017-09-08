# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User as DjangoUser

class User(DjangoUser):
    # 新規にtableを作成せずに継承したmodelの拡張のみを行う
    class Meta:
        proxy = True

    # 自分がフォローしてる人たち
    def followees(self):
        follows = Follow.objects.filter(from_user=self, deleted=False)
        return [follow.to_user for follow in follows]

    # 自分をフォローしてくれてる人たち
    def followers(self):
        follows = Follow.objects.filter(to_user=self, deleted=False)
        return [follow.from_user for follow in follows]

class Tweet(models.Model):
    text = models.CharField(max_length=140)
    user_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', null=True)
    to_user = models.ForeignKey(User, related_name='to_user', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
