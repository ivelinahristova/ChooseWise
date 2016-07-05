from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'add$', views.add, name='add'),
    url(r'consumed$', views.consumed, name='consumed'),
    url(r'list/$', views.list, name='list'),
    url(r'suggest/$', views.suggest, name='suggest'),
    url(r'nutrients/$', views.nutrients, name='nutrients'),
    url(r'diet/$', views.diet_add, name='diet_add'),
    url(r'diet/delete/(?P<diet_id>[0-9]+)/$', views.diet_delete, name='diet_add'),
]