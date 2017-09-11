# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /api/user/harada/
    url(r'^user/harada/$', views.user_harada, name='user_harada'),
    # ex: /pakutter/tweet/1/
    url(r'^user/(?P<user_id>[0-9]+)/$', views.user_data, name='user_data'),
]
