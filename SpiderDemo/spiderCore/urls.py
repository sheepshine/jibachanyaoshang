# coding:utf8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^article/add$', views.add_article),
    url(r'^article/start_request', views.start_request)
]