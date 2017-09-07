# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required

from .models import Tweet

@login_required
def index(request):
    tweet_list = Tweet.objects.filter(user_id=request.user.id)
    # TODO とりあえず自分のツイートだけ見える
    # TODO Tweetを取ってくるルール 自分の+フォロー中の
    # TODO order_by 日付 最新が上に来るようにする

    template = loader.get_template('index.html')
    context = {
        'user_name' : request.user.username,
        'tweet_list': tweet_list,
    }
    return HttpResponse(template.render(context, request))

@login_required
def user(request, user_id):
    tweet_list = Tweet.objects.filter(user_id=user_id)
    template = loader.get_template('user.html')
    context = {
        # TODO idに対応したユーザーを取ってくる
        'user_name' : request.user.username,
        'tweet_list': tweet_list,
    }
    return HttpResponse(template.render(context, request))

@login_required
def tweet(request):
    if request.method == "POST":
        tweet =  Tweet(
          text = request.POST['new_tweet'],
          user_id = request.user.id
          )
        tweet.save()
    return HttpResponseRedirect('../')
