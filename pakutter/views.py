# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Tweet

from .forms import MyForm

def index(request):
    tweet_list = Tweet.objects.order_by('id')
    template = loader.get_template('index.html')
    context = {
        'tweet_list': tweet_list,
    }
    return HttpResponse(template.render(context, request))

def user(request, user_id):
    # TODO
    response = "ユーザーID%s"
    return HttpResponse(response % user_id)

def tweet(request):
    if request.method == "POST":
        tweet =  Tweet(text=request.POST['new_tweet'])
        tweet.save()
    return redirect('index')
