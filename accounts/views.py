# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from pakutter.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password

def register(request):
    template = loader.get_template('register.html')
    context = {}
    return HttpResponse(template.render(context, request))

def create_new_user(request):
    # TODO
    # バリデーションエラーっぽくなった場合エラーになってしまう
    if request.method == "POST":
        new_user = User.objects.create(
          username = request.POST['username'],
          password = make_password(request.POST['password']) #ハッシュ化して登録
          )
        new_user.save()
    return HttpResponseRedirect('../../login')
