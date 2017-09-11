# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /api/user_data/
    url(r'^user_data/$', views.user_data, name='user_data'),
]
