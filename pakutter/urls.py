# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /pakutter/
    url(r'^$', views.index, name='index'),
    # ex: /pakutter/user/1/
    url(r'^user/(?P<user_id>[0-9]+)/$', views.user, name='user'),
    # ex: /pakutter/user/1/follow
    url(r'^user/(?P<user_id>[0-9]+)/follow/$', views.follow, name='follow'),
    # ex: /pakutter/user/1/unfollow
    url(r'^user/(?P<user_id>[0-9]+)/unfollow/$', views.unfollow, name='unfollow'),
    # ex: /pakutter/users/
    url(r'^users/$', views.users, name='users'),
    # ex: /pakutter/tweet/
    url(r'^tweet/$', views.tweet, name='tweet'),
    # ex: /pakutter/tweet/1/
    url(r'^tweet/(?P<tweet_id>[0-9]+)/$', views.tweet_detail, name='detail'),
]
