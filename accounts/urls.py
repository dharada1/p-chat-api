from django.conf.urls import url
from django.contrib.auth.views import login,logout

from . import views

urlpatterns = [
    # ex: /register/
    url(r'^register/$', views.register, name='register'),
    # ex: /register/create_new_user/
    url(r'^register/create_new_user/$', views.create_new_user, name='create_new_user'),
    # ex: /login/
    url(r'^login/$', login,
        {'template_name': 'login.html'},
        name='login'),
    # ex: /logout/
    url(r'^logout/$', logout,
        {'template_name': 'login.html'},
        name='logout')
]
