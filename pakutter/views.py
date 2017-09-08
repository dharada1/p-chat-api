# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required

from django.db.models import Q

from .models import Tweet, Follow, User

# トップページ(タイムライン)
@login_required
def index(request):
    # TODO request.userがinheritしたuserのオブジェクトでないので.followeesメソッドが使えない...がんばれば解決出来そう
    # http://scottbarnham.com/blog/2008/08/21/extending-the-django-user-model-with-inheritance.1.html
    inherited_request_user_query = User.objects.filter(id=request.user.id)
    inherited_request_user = inherited_request_user_query.first()

    followees = inherited_request_user.followees()

    # TODO 自分のあつかい...
    # followees_and_request_user = followees.append(inherited_request_user) したい

    # followeesが発言したツイートのリストを作成
    queries = [Q(user=user) for user in followees]
    query = queries.pop()
    for item in queries:
      query |= item
    tweet_list = Tweet.objects.filter(query).order_by('created_at').reverse()

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
    tweet_list = Tweet.objects.filter(user=user).order_by('created_at').reverse()

    template = loader.get_template('user.html')
    context = {
        'login_user' : request.user,
        'user' : user,
        'tweet_list': tweet_list,
        'followers' : user.followers,
        'followees' : user.followees,
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
    if request.method == "POST" and request.POST['new_tweet'] != "":
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
        user_to_follow = User.objects.filter(id=user_id).first()
        Follow.objects.update_or_create(
          from_user = request.user,
          to_user = user_to_follow,
          deleted = False
          )
    return HttpResponseRedirect('../')

# リムーブ(アンフォロー)
@login_required
def unfollow(request, user_id):
    if request.method == "POST":
        user_to_unfollow = User.objects.filter(id=user_id).first()
        follow = Follow.objects.filter(
          from_user=request.user,
          to_user=user_to_unfollow,
          deleted=False
          ).first()
        if follow:
          follow.deleted = True
          follow.save()
    return HttpResponseRedirect('../')

# tweet毎の詳細画面
@login_required
def tweet_detail(request, tweet_id):
    tweet = Tweet.objects.filter(id = tweet_id).first()
    poster = User.objects.filter(id=tweet.user_id).first()

    template = loader.get_template('tweet_detail.html')
    context = {
        'login_user' : request.user,
        'tweet' : tweet,
        'poster' : poster,
    }
    return HttpResponse(template.render(context, request))
