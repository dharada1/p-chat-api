# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json
from collections import OrderedDict
from django.http import HttpResponse
from .models import DummyUser, Message

from datetime import datetime
import time
import calendar
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

# ユーザーデータをGETする
def user_data(request, user_id):
    user = DummyUser.objects.filter(id = user_id).first()

    data = OrderedDict([
      ('user_id', int(user_id)),
      ('user_name', user.name),
      ('gender', user.gender),
      ('age', user.age),
      ('job', user.job),
    ])

    return render_json_response(request, data)

# message historyを返す部分
def message_history(request):
    #requestからuser_idとpartner_idを受け取る。
    user_id    = request.GET.get("user_id")
    partner_id = request.GET.get("partner_id")

    user    = DummyUser.objects.filter(id = user_id).first()
    partner = DummyUser.objects.filter(id = partner_id).first()

    #ユーザーとパートナーが存在していたら
    if user and partner:
      # TODO いまはとりあえずuser_idに一致するやつだけ取ってきている。
      # select where user1 partner2  user2 partner1
      messages = Message.objects.filter(id = user_id)

      # Messageが無かったらmessagesの値は"empty"という文字列。
      # Messageが存在していたら、messagesの値はmessageが詰まったlistになる。
      if messages:
        messages_for_return = []
        for message in messages:
          tstr = message.created_at.strftime('%Y-%m-%d %H:%M:%S')
          tdatetime = datetime.strptime(tstr,'%Y-%m-%d %H:%M:%S')

          message_for_return = OrderedDict([
            ('id', message.id),
            ('user_id', message.user.id),
            ('partner_id', message.partner.id),
            ('from_me', message.from_me),
            ('content', message.content),
            ('created_at',calendar.timegm(tdatetime.timetuple())), # Unixtimeで返す
          ])
          messages_for_return.append(message_for_return)
        # TODO messages_for_returnをID順にソート。上の方が新しいMessageとなるようにする。
      else:
        messages_for_return = "empty"

      # returnするデータ
      data = OrderedDict([
        ('user_id', user.id),
        ('partner_id', partner.id),
        ('messages', messages_for_return),
      ])
    else:
      data = {"status":"error"}

    return render_json_response(request, data)

#messageをデータベースに登録
@csrf_exempt
def message_create(request):
    if "content" in request.POST:
        # query_paramが指定されている場合の処理
        user_id = request.POST.get("user_id")
        partner_id = request.POST.get("partner_id")
        content = request.POST.get("content")

        #create
        Message.objects.create(
          user = DummyUser.objects.filter(id = user_id).first(),
          partner = DummyUser.objects.filter(id = partner_id).first(),
          content = content,
          # from_me 必ず 1 としておく(つまり、userが送り手側 / partnerが受け手側 ということ)
          from_me = 1,
        )

        resultdict = {"status":"success"}

    else:
        # query_paramが指定されていない場合の処理
        resultdict = {"status":"error"}

    return render_json_response(request,resultdict)
