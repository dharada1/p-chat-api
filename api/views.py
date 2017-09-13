# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json
from collections import OrderedDict
from django.http import HttpResponse
from .models import DummyUser, Message

# 参考: Python Django入門 (6) JSONを返すAPIの部分
# http://qiita.com/kaki_k/items/b76acaeab8a9d935c35c

# JSON整形を行う関数
def render_json_response(request, data, status=None):
    """response を JSON で返却"""
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')  # POSTでJSONPの場合
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    return response

# 原田のユーザーデータを返すサンプル
def user_harada(request):
    user_name = u'原田大地'
    age = 23
    job = u'エンジニア'

    communities = [u'北海道に住んでいる', u'Twitterをやっている', u'TOFUBEATSが好き']

    comment = u'焼肉食べたい'

    data = OrderedDict([
      ('user_name', user_name),
      ('communities', communities),
      ('age', age),
      ('job', job),
      ('comment', comment),
    ])

    return render_json_response(request, data)

# user_idとか引数に取っていろいろやるやつのサンプル
def user_data(request, user_id):
    user_name = u'ユーザー' + str(user_id)

    data = OrderedDict([
      ('user_id', user_id),
      ('user_name', user_name),
    ])

    return render_json_response(request, data)

# message historyを返す部分
def message_history(request):
    # dummy user
    user1 = DummyUser.objects.create(
      name = u"原田大地",
      gender = 1,
      job = u"学生",
    )
    # dummy partner
    user2 = DummyUser.objects.create(
      name = u"山田はなこ",
      gender = 2,
      job = u"会社員",
    )

    # dummy message
    message1 = Message.objects.create(
      user = user1,
      partner = user2,
      from_me = 1,
      content = u"こんにちは！",
      )
    # dummy message
    message2 = Message.objects.create(
      user = user1,
      partner = user2,
      from_me = 2,
      content = u"熱盛！",
      )

    # messageをreturnするため整形する
    messages = [message1, message2]
    messages_for_return = []
    for message in messages:
      message_for_return = OrderedDict([
        ('user_id', message.user.id),
        ('partner_id', message.partner.id),
        ('from_me', message.from_me),
        ('content', message.content),
        ('created_at', message.created_at.strftime('%Y-%m-%d %H:%M:%S')), # 返却方法要相談
      ])
      messages_for_return.append(message_for_return)

    # returnするデータ
    data = OrderedDict([
      ('user_id', user1.id),
      ('partner_id', user2.id),
      ('messages', messages_for_return),
    ])

    return render_json_response(request, data)
