from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'login/$', views.sign_in, name='sign_in'),
    url(r'logout/$', views.sign_out, name='sign_out'),
    url(r'profile/$', views.profile, name='profile'),
]
