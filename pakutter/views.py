# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required

from .models import Tweet, Follow
from django.contrib.auth.models import User

# トップページ(タイムライン)
@login_required
def index(request):
    tweet_list = Tweet.objects.filter(user_id=request.user.id).order_by('created_at').reverse()
    # TODO とりあえず自分のツイートだけ見える
    # TODO Tweetを取ってくるルール 自分の+フォロー中の
    template = loader.get_template('index.html')
    context = {
        'login_user' : request.user,
        'tweet_list': tweet_list,
    }
    return HttpResponse(template.render(context, request))

# ユーザー毎の詳細画面
@login_required
def user(request, user_id):
    user = User.objects.filter(id = user_id).first()
    tweet_list = Tweet.objects.filter(user_id=user_id).order_by('created_at').reverse()
    template = loader.get_template('user.html')
    context = {
        'login_user' : request.user,
        'user' : user,
        'tweet_list': tweet_list,
    }
    return HttpResponse(template.render(context, request))

# ユーザー一覧画面
@login_required
def users(request):
    user_list = User.objects.order_by('id')
    template = loader.get_template('users.html')
    context = {
        'login_user' : request.user,
        'user_list' : user_list,
    }
    return HttpResponse(template.render(context, request))

# ツイート
@login_required
def tweet(request):
    if request.method == "POST":
        tweet =  Tweet(
          text = request.POST['new_tweet'],
          user_id = request.user.id
          )
        tweet.save()
    return HttpResponseRedirect('../')

# フォロー
@login_required
def follow(request, user_id):
    if request.method == "POST":
        # TODO 同一のフォローデータが無かったらフォローするようにする
        follow =  Follow(
          from_id = request.user.id,
          to_id = user_id,
          )
        follow.save()

    # TODO 適切なリダイレクト先考える
    return HttpResponseRedirect('../')
