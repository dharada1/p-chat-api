# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from collections import OrderedDict
from django.http import HttpResponse
from .models import DummyUser, Message
from django.db.models import Q
from datetime import datetime
import time
import calendar

'''
API

各々の関数でデータを詰め込んだdictをつくり、
それをrender_json_responseに渡してJSONに整形してreturnする。

参考: Python Django入門 (6) JSONを返すAPIの部分
http://qiita.com/kaki_k/items/b76acaeab8a9d935c35c
'''

# response を JSON で返却
def render_json_response(request, data, status=None):
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
# messageが id順(時系列) で返される
def message_history(request):
    #requestからuser_idとpartner_idを受け取る。
    user_id    = request.GET.get("user_id")
    partner_id = request.GET.get("partner_id")

    user    = DummyUser.objects.filter(id = user_id).first()
    partner = DummyUser.objects.filter(id = partner_id).first()

    if user and partner:
      # select where user1 partner2  user2 partner1
      # user->partner のメッセージ, partner->user のメッセージ両方取る
      messages = Message.objects.filter(
        Q(user_id = user_id, partner_id = partner_id) | Q(user_id = partner_id, partner_id = user_id)
      ).order_by('id')

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
            ('content', message.content),
            ('created_at',calendar.timegm(tdatetime.timetuple())), # Unixtimeで返す
          ])
          messages_for_return.append(message_for_return)
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
