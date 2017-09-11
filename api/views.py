# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json
from collections import OrderedDict
from django.http import HttpResponse

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

    data = OrderedDict([
      ('user_name', user_name),
      ('communities', communities),
      ('age', age),
      ('job', job),
    ])

    return render_json_response(request, data)

#
def user_data(request, user_id):
    user_name = u'ユーザー' + str(user_id)

    data = OrderedDict([
      ('user_id', user_id),
      ('user_name', user_name),
    ])

    return render_json_response(request, data)
