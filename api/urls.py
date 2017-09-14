# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /api/user/1/
    url(r'^user/(?P<user_id>[0-9]+)/$', views.user_data, name='user_data'),
    # ex: /api/message/create/
    url(r'^message/create/$', views.message_create, name='message_create'),
    # ex: /api/message/history/
    url(r'^message/history/$', views.message_history, name='message_history'),
    # ex: /api/message/reset/
    url(r'^message/reset/$', views.message_reset, name='message_reset'),

]
