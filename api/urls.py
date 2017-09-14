# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /api/message/history/
    url(r'^message/history/$', views.message_history, name='message_history'),
    # ex: /api/message/create/
    url(r'^message/create/$', views.message_create, name='message_create'),
    #ダミー
    # ex: /api/message/history_dummy/
    #url(r'^message/history_dummy/$', views.message_history_dummy, name='message_history_dummy'),
    # ex: /api/user/1/
    url(r'^user/(?P<user_id>[0-9]+)/$', views.user_data, name='user_data'),
]
