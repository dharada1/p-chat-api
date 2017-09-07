# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required

from .models import Tweet
from django.contrib.auth.models import User

@login_required
def index(request):
    tweet_list = Tweet.objects.filter(user_id=request.user.id).order_by('created_at').reverse()
    # TODO とりあえず自分のツイートだけ見える
    # TODO Tweetを取ってくるルール 自分の+フォロー中の

    template = loader.get_template('index.html')
    context = {
        'user_name' : request.user.username,
        'tweet_list': tweet_list,
    }
    return HttpResponse(template.render(context, request))

@login_required
def user(request, user_id):
    user = User.objects.filter(id = user_id).first()
    tweet_list = Tweet.objects.filter(user_id=user_id).order_by('created_at').reverse()
    template = loader.get_template('user.html')
    context = {
        # TODO idに対応したユーザーを取ってくる
        'user_name' : user.username,
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
