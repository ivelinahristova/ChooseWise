from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list, name='index'),
    url(r'list/$', views.list, name='list'),
    url(r'nutrients/$', views.nutrients, name='nutrients'),
]