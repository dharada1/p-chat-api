# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /api/user/harada/
    url(r'^user/harada/$', views.user_harada, name='user_harada'),
    # ex: /api/message/history/
    url(r'^message/history/$', views.message_history, name='message_history'),
    #ダミー
    # ex: /api/message/history_dummy/
    #url(r'^message/history_dummy/$', views.message_history_dummy, name='message_history_dummy'),
    # ex: /api/user/1/
    url(r'^user/(?P<user_id>[0-9]+)/$', views.user_data, name='user_data'),
]
