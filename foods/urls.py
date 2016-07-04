from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'add$', views.add, name='add'),
    url(r'consumed$', views.consumed, name='consumed'),
    url(r'list/$', views.list, name='list'),
    url(r'nutrients/$', views.nutrients, name='nutrients'),
]