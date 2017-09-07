# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Tweet(models.Model):
    text = models.CharField(max_length=140)
    user_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    from_id = models.IntegerField(default=0)
    to_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    # フォロイー(フォローしてる人)のid_listを返す。
    @classmethod
    def followee_id_list(self, user_id):
      follow_list = Follow.objects.filter(from_id=user_id)
      id_list = []
      for follow in follow_list:
        id_list.append(follow.to_id)
      return id_list

    # フォロワー(フォローされてる人)のid_listを返す
    @classmethod
    def follower_id_list(self, user_id):
      follow_list = Follow.objects.filter(to_id=user_id)
      id_list = []
      for follow in follow_list:
        id_list.append(follow.from_id)
      return id_list
