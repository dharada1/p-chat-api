# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /pakutter/
    url(r'^$', views.index, name='index'),
    # ex: /pakutter/user/1/
    url(r'^user/(?P<user_id>[0-9]+)/$', views.user, name='user'),
    # ex: /pakutter/tweet/1/
    url(r'^tweet/(?P<tweet_id>[0-9]+)/$', views.tweet, name='tweet'),
]
